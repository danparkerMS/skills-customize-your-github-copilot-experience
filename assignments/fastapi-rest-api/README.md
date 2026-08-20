# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a small collection of books. You will practice defining routes, validating request data, returning HTTP status codes, and handling missing resources with FastAPI.

## 📝 Tasks

### 🛠️ Create Read Endpoints

#### Description
Complete the API routes that let clients check the service status and retrieve the full book collection.

#### Requirements
Completed program should:

- Implement `GET /` and return a welcome message
- Implement `GET /books` and return every book in the collection
- Return JSON responses that can be viewed in FastAPI's interactive documentation at `/docs`

### 🛠️ Add Books with Validation

#### Description
Create an endpoint that accepts a validated book request and adds a new book to the in-memory collection.

#### Requirements
Completed program should:

- Implement `POST /books` using the provided `BookCreate` request model
- Assign each new book a unique integer ID
- Add the new book to the collection and return it with HTTP status `201 Created`
- Reject requests that omit the title, author, or publication year

### 🛠️ Manage Individual Books

#### Description
Add routes that retrieve and delete one book by its ID while returning clear errors when the requested book does not exist.

#### Requirements
Completed program should:

- Implement `GET /books/{book_id}` and return the matching book
- Implement `DELETE /books/{book_id}` and remove the matching book
- Return HTTP status `404 Not Found` with a clear message for an unknown book ID
- Return HTTP status `204 No Content` after a successful deletion