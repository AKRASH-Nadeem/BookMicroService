# gRPC Book Service

A simple gRPC service for managing a collection of books, built using Protocol Buffers and Python. This service allows clients to perform CRUD (Create, Read, Update, Delete) operations on books.

## Features

- Add new books to the collection
- Retrieve books by ID
- Update existing book details
- Delete books from the collection

## Technologies Used

- Python 3.x
- gRPC
- Protocol Buffers

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AKRASH-Nadeem/BookMicroService.git
   cd BookMicroService
2. **Install the required packages:**
    ```bash
    pip install grpcio grpcio-tools
    ```
3. **Generate the gRPC code from the .proto file:**
    ```bash
    python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. book_service.proto
    ```
## Usage
### Running the Server
To start the gRPC server, run the following command:
```bash
python server.py
```
The server will start on port ``50051``.
### Running the Client
Open another terminal and run the client to interact with the server:
```bash
python client.py
```
### Example Output
When you run the client, you should see output similar to the following:
```bash
Book Added!
Retrieved Book:
 id: 1
title: "The Great Gatsby"
author: "F. Scott Fitzgerald"
description: "A novel set in the Roaring Twenties."
publication_year: 1925

Book Updated
Book Deleted!
```
## API Reference
### BookService
**AddBook**
- Request: ``AddBookRequest``
- Response: ``AddBookResponse``

**GetBook**
- Request: ``GetBookRequest``
- Response: ``GetBookResponse``

**UpdateBook**
- Request: ``UpdateBookRequest``
- Response: ``UpdateBookResponse``

**DeleteBook**
- Request: ``DeleteBookRequest``
- Response: ``DeleteBookResponse``