# main.py
# FastAPI 백엔드 - Library CRUD API

from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from . import database

app = FastAPI(title="Library Management API")


class BookBase(BaseModel):
    title: str
    author: Optional[str] = None
    year: Optional[int] = None
    available: Optional[int] = 1


class Book(BookBase):
    id: int


@app.on_event("startup")
def on_startup():
    database.init_db()


@app.get("/books", response_model=List[Book])
def list_books():
    books = database.get_all_books()
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = database.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books", response_model=Book)
def create_book(book: BookBase):
    new_id = database.create_book(book.title, book.author or "", book.year or 0)
    created = database.get_book(new_id)
    return created


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookBase):
    existing = database.get_book(book_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Book not found")
    database.update_book(
        book_id,
        book.title,
        book.author or "",
        book.year or 0,
        book.available if book.available is not None else 1,
    )
    updated = database.get_book(book_id)
    return updated


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    existing = database.get_book(book_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Book not found")
    database.delete_book(book_id)
    return {"detail": "Book deleted"}
Запуск:
uvicorn faker_db_crud.main:app --reload --port 8000
