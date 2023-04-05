# Write a test that checks if a function runs in a certain amount of time.

import pytest
import time
import requests


def test_performance():
    start_time = time.time()

    response = requests.get("https://www.example.com/404")
    assert response.status_code == 404

    end_time = time.time()
    assert end_time - start_time < 2.0
