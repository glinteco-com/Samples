import models
import schemas
from sqlalchemy.orm import Session


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_book_by_author(db: Session, author: str):
    return db.query(models.Book).filter(models.Book.author == author).first()


def get_book_by_title_author(db: Session, title: str, author: str):
    return (
        db.query(models.Book)
        .filter(models.Book.title == title, models.Book.author == author)
        .first()
    )


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(author=book.author, price=book.price, title=book.title)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
