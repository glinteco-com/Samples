import tasks
from celery.result import AsyncResult
from flask import Blueprint, render_template, request

home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.route("/")
def index():
    return render_template(
        "index.html",
    )


@home_blueprint.route("/tasks/<id>")
def task_result(id: str) -> dict[str, object]:
    task_result = AsyncResult(id)
    return {"ready": task_result.ready()}


@home_blueprint.route("/add-numbers", methods=["POST"])
def add_numbers() -> dict[str, object]:
    data = request.json
    task = tasks.add_numbers.delay(data["number1"], data["number2"])
    return {"task_id": task.id}
