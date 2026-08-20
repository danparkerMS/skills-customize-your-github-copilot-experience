from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(title="Book Collection API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0)


class Book(BookCreate):
    id: int


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", year=1962),
]


@app.get("/")
def read_root():
    # TODO: Return a welcome message.
    pass


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Assign a unique ID, save the book, and return it.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the matching book or raise HTTPException with status 404.
    return Response(status_code=status.HTTP_204_NO_CONTENT)