import grpc

# Import the generated classes
import book_service_pb2
import book_service_pb2_grpc

def run():
    # Create a channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_service_pb2_grpc.BookServiceStub(channel)

        # Add a new book
        new_book = book_service_pb2.Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A novel set in the Roaring Twenties.", publication_year=1925)
        response = stub.AddBook(book_service_pb2.AddBookRequest(book=new_book))
        print(response.status)

        # Get the book
        get_response = stub.GetBook(book_service_pb2.GetBookRequest(id=1))
        print("Retrieved Book:\n", get_response.book)

        # Update the book
        updated_book = book_service_pb2.Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A classic novel of the Jazz Age.", publication_year=1925)
        update_response = stub.UpdateBook(book_service_pb2.UpdateBookRequest(book=updated_book))
        print(update_response.status)

        # Delete the book
        delete_response = stub.DeleteBook(book_service_pb2.DeleteBookRequest(id=1))
        print(delete_response.status)

if __name__ == '__main__':
    run()
