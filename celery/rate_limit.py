"""
This code snippet offers a custom Celery Task designed to prevent multiple concurrent executions of a task with identical parameters within a specific timeframe.

It accomplishes this through the following steps:
1. Upon the initial execution of the task, the class generates a unique key for each combination of the task name and its parameters, creating a counter that is then stored in the cache system.
2. Subsequent triggers of the task with the same parameters within an acceptable timeframe will increase the counter.
3. If the counter reaches the maximum value, any subsequent tasks will be ignored.
4. Upon the task's completion, regardless of success or failure, the counter will be reduced.

#! pip install celery django 
"""

import logging
import base64
import time
from contextlib import contextmanager
from datetime import datetime

from celery import Task
from celery.exceptions import Ignore
from django.core.cache import cache


logger = logging.getLogger(__name__)


@contextmanager
def memcache_lock(lock_id, oid, lock_expire):
    timeout_at = time.monotonic() + lock_expire
    status = cache.add(lock_id, oid, lock_expire)
    try:
        yield status
    finally:
        if time.monotonic() < timeout_at and status:
            # don't release the lock if we exceeded the timeout
            # to lessen the chance of releasing an expired lock
            # owned by someone else
            # also don't release the lock if we didn't acquire it
            cache.delete(lock_id)


class RateLimitTask(Task):
    LOCK_KEY_TEMPLATE = "celery:rate_limit_task-{0}"
    RATELIMIT = {  # how many tasks per timeframe
        "tasks": 4,
        "time": 60,  # in seconds
    }

    def __call__(self, *args, **kwargs):
        """The body of the task executed by workers."""

        rate_limit = self.RATELIMIT
        custom_rate_limit = getattr(self, "custom_rate_limit", None)
        if custom_rate_limit:
            rate_limit = custom_rate_limit

        base_task_id = self.generate_lock_id(*args, **kwargs)
        first_task_at_lock_id = f"{base_task_id}-first_task_at"
        count_tasks_lock_id = f"{base_task_id}-count_tasks"

        first_task_at = cache.get(first_task_at_lock_id)
        count_tasks = cache.get(count_tasks_lock_id, 0)

        now = datetime.now()

        if not first_task_at:  # first_task_at will be automatically timeout
            first_task_at = now
            count_tasks = 0
            cache.set(first_task_at_lock_id, first_task_at, rate_limit["time"])
            cache.set(count_tasks_lock_id, count_tasks, rate_limit["time"])

        time_from_first_task = (now - first_task_at).total_seconds()
        valid_to_run = (
            time_from_first_task < rate_limit["time"]
            and count_tasks < rate_limit["tasks"]
        )
        if valid_to_run:
            cache.incr(count_tasks_lock_id)
            return self.run(*args, **kwargs)

        logger.warning(
            f"Reach rate limit: {count_tasks}/{rate_limit['tasks']} "
            f"per {rate_limit['time']}s with task_id: {base_task_id}"
        )
        raise Ignore()

    def generate_lock_id(self, *args, **kwargs):
        keys = [self.LOCK_KEY.format(self.name)]

        for arg in args:
            keys.append(str(arg))
        for key, value in kwargs.items():
            keys.append("{}={}".format(key, value))

        result_string = "&".join(keys)
        result_string = base64.b64encode(result_string.encode())

        return result_string

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        lock_id = self.generate_lock_id(*args, **kwargs)
        self.release_lock(lock_id)
        return super().after_return(
            status, retval, task_id, args, kwargs, einfo
        )

    def release_lock(self, lock_id):
        cache.delete(lock_id)
