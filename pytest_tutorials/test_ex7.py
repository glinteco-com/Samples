# Write a test that checks if a web page returns a 404 error.

import pytest
import requests


def test_404():
    response = requests.get("https://www.example.com/404")
    assert response.status_code == 404
