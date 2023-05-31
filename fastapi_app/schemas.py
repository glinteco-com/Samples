from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str | None = None
    price: float | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
