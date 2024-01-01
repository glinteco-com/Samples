"""
This code snippet offers a custom Celery Task designed to prevent multiple concurrent executions of a task with identical parameters.

It accomplishes this through the following steps:
1. Upon the initial execution of the task, the class generates a unique key for each combination of the task name and its parameters, creating a lock that is then stored in the cache system.
2. Subsequent triggers of the task with the same parameters within an acceptable timeframe will be ignored.
3. Upon the task's completion, regardless of success or failure, the lock will be released.

#! pip install celery django 
"""

import base64
import time
from contextlib import contextmanager

from celery import Task
from celery.exceptions import Ignore
from django.core.cache import cache


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


class UniqueCeleryTask(Task):
    LOCK_KEY = "celery:base_unique_task-{0}"
    LOCK_EXPIRE = 60 * 10  # minutes

    def __call__(self, *args, **kwargs):
        """The body of the task executed by workers."""

        lock_expire = self.LOCK_EXPIRE

        custom_lock_expire = getattr(self, "custom_lock_expire", None)
        if custom_lock_expire:
            lock_expire = custom_lock_expire

        lock_id = self.generate_lock_id(*args, **kwargs)

        with memcache_lock(lock_id, self.app.oid, lock_expire) as acquired:
            if acquired:
                return self.run(*args, **kwargs)
            else:
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
