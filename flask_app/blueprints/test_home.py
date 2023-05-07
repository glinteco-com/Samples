import json

from flask import url_for


def test_index(client):
    response = client.get(url_for("home.index"))
    assert response.status_code == 200


def test_task_result(client):
    response = client.get(url_for("home.task_result", id=123))

    assert response.status_code == 200


def test_add_numbers(client, headers):
    data = {"number1": 2, "number2": 3}

    response = client.post(
        url_for("home.add_numbers"), data=json.dumps(data), headers=headers
    )

    assert response.status_code == 200
    assert "task_id" in response.json
