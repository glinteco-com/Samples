import pytest
from app import create_app, db
from models import Book


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


@pytest.fixture
def default_book():
    existed_book = Book.query.filter_by(title="Flask app1").first()
    if existed_book:
        return existed_book

    book = Book(title="Flask app1", author="Joe")
    db.session.add(book)
    db.session.commit()

    return book
