from app import db
from flask import request
from flask_restful import Resource
from models import Book
from schemas import BookSchema


class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return BookSchema().dump(book)

    def put(self, book_id):
        book = Book.query.get_or_404(book_id)
        data = request.json
        book.title = data["title"]
        book.author = data["author"]
        db.session.commit()
        return BookSchema().dump(book)

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return "", 204


class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return BookSchema(many=True).dump(books)

    def post(self):
        data = request.json
        book = Book(title=data["title"], author=data["author"])
        db.session.add(book)
        db.session.commit()
        return BookSchema().dump(book), 201
