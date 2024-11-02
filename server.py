import grpc
from concurrent import futures
import time

# Import the generated classes
import book_service_pb2
import book_service_pb2_grpc

# A simple in-memory book storage
books = {}

class BookService(book_service_pb2_grpc.BookServiceServicer):
    
    def AddBook(self, request, context):
        book_id = request.book.id
        books[book_id] = request.book
        return book_service_pb2.AddBookResponse(status="Book Added!", book=request.book)
    
    def GetBook(self, request, context):
        book_id = request.id
        book = books.get(book_id)
        if book:
            return book_service_pb2.GetBookResponse(book=book)
        else:
            context.set_details("book not found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_service_pb2.GetBookResponse()

    def UpdateBook(self, request, context):
        book_id = request.book.id
        if book_id in books:
            books[book_id] = request.book
            return book_service_pb2.UpdateBookResponse(status="Book Updated",book=request.book)
        else:
            context.set_details("Book Not Found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_service_pb2.UpdateBookResponse()

    def DeleteBook(self, requst, context):
        book_id = requst.id
        if book_id in books:
            del books[book_id]
            return book_service_pb2.DeleteBookResponse(status="Book Deleted!")
        else:
            context.set_details("Book Not Found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_service_pb2.DeleteBookResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_service_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server is running on port 50051...")
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()