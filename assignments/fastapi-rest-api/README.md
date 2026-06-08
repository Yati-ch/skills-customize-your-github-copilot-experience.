# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, high-performance REST APIs using FastAPI framework. You will create a simple API for managing a collection of books, implementing GET, POST, PUT, and DELETE endpoints while practicing data validation and error handling.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project

#### Description
Set up a new FastAPI project with the necessary dependencies and create a basic server that responds to requests.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn using pip
- Create a `main.py` file with a FastAPI application instance
- Implement a root endpoint (`/`) that returns a welcome message with JSON format
- Run the server using Uvicorn and verify it responds to requests
- Example response: `{"message": "Welcome to the Book API"}`

### 🛠️ Create Book Model and In-Memory Storage

#### Description
Define a Book data model using Pydantic and create an in-memory list to store books.

#### Requirements
Completed program should:

- Create a `Book` Pydantic model with fields: `id` (int), `title` (str), `author` (str), `isbn` (str), and `published_year` (int)
- Initialize an empty list to store books in memory
- Add validation: ensure `title` and `author` are not empty strings
- Add validation: ensure `published_year` is a valid year (between 1000 and current year)

### 🛠️ Implement GET Endpoints

#### Description
Create endpoints to retrieve books from the API.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books as a JSON array
- Implement `GET /books/{book_id}` to return a specific book by ID
- Return appropriate HTTP status code 404 when a book is not found
- Include a response with error message: `{"detail": "Book not found"}`
- Example: `GET /books/1` returns `{"id": 1, "title": "...", "author": "...", "isbn": "...", "published_year": 2020}`

### 🛠️ Implement POST Endpoint

#### Description
Create an endpoint to add new books to the collection.

#### Requirements
Completed program should:

- Implement `POST /books` to create a new book
- Auto-generate book IDs (starting from 1)
- Validate request data using Pydantic model
- Return the created book object with HTTP status code 201
- Handle validation errors with appropriate error messages

### 🛠️ Implement PUT Endpoint

#### Description
Create an endpoint to update existing book information.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update a book
- Only update fields provided in the request (partial updates allowed)
- Return the updated book object
- Return HTTP status code 404 if the book does not exist
- Validate all provided fields before updating

### 🛠️ Implement DELETE Endpoint

#### Description
Create an endpoint to remove books from the collection.

#### Requirements
Completed program should:

- Implement `DELETE /books/{book_id}` to delete a book
- Return HTTP status code 204 (No Content) on successful deletion
- Return HTTP status code 404 if the book does not exist
- Verify the book is removed from the collection after deletion

