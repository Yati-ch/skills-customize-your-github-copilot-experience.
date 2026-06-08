from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# TODO: Define the Book model using Pydantic
# The model should include: id, title, author, isbn, published_year


# TODO: Create an in-memory list to store books
books = []


# TODO: Implement the root endpoint that returns a welcome message
@app.get("/")
def read_root():
    pass


# TODO: Implement GET /books endpoint to return all books


# TODO: Implement GET /books/{book_id} endpoint to return a specific book


# TODO: Implement POST /books endpoint to create a new book


# TODO: Implement PUT /books/{book_id} endpoint to update a book


# TODO: Implement DELETE /books/{book_id} endpoint to delete a book
