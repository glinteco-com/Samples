from flask import url_for


def test_books_list(client, default_book):
    response = client.get(url_for("booklistresource"))

    assert response.status_code == 200
    book_ids = [item["id"] for item in response.json]
    assert default_book.id in book_ids


def test_book_detail(client, default_book):
    response = client.get(url_for("bookresource", book_id=default_book.id))

    assert response.status_code == 200
    assert default_book.id == response.json["id"]
