# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import book_service_pb2 as book__service__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in book_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddBook = channel.unary_unary(
                '/bookservice.BookService/AddBook',
                request_serializer=book__service__pb2.AddBookRequest.SerializeToString,
                response_deserializer=book__service__pb2.AddBookResponse.FromString,
                _registered_method=True)
        self.GetBook = channel.unary_unary(
                '/bookservice.BookService/GetBook',
                request_serializer=book__service__pb2.GetBookRequest.SerializeToString,
                response_deserializer=book__service__pb2.GetBookResponse.FromString,
                _registered_method=True)
        self.UpdateBook = channel.unary_unary(
                '/bookservice.BookService/UpdateBook',
                request_serializer=book__service__pb2.UpdateBookRequest.SerializeToString,
                response_deserializer=book__service__pb2.UpdateBookResponse.FromString,
                _registered_method=True)
        self.DeleteBook = channel.unary_unary(
                '/bookservice.BookService/DeleteBook',
                request_serializer=book__service__pb2.DeleteBookRequest.SerializeToString,
                response_deserializer=book__service__pb2.DeleteBookResponse.FromString,
                _registered_method=True)


class BookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddBook': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBook,
                    request_deserializer=book__service__pb2.AddBookRequest.FromString,
                    response_serializer=book__service__pb2.AddBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=book__service__pb2.GetBookRequest.FromString,
                    response_serializer=book__service__pb2.GetBookResponse.SerializeToString,
            ),
            'UpdateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBook,
                    request_deserializer=book__service__pb2.UpdateBookRequest.FromString,
                    response_serializer=book__service__pb2.UpdateBookResponse.SerializeToString,
            ),
            'DeleteBook': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBook,
                    request_deserializer=book__service__pb2.DeleteBookRequest.FromString,
                    response_serializer=book__service__pb2.DeleteBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bookservice.BookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('bookservice.BookService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bookservice.BookService/AddBook',
            book__service__pb2.AddBookRequest.SerializeToString,
            book__service__pb2.AddBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bookservice.BookService/GetBook',
            book__service__pb2.GetBookRequest.SerializeToString,
            book__service__pb2.GetBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bookservice.BookService/UpdateBook',
            book__service__pb2.UpdateBookRequest.SerializeToString,
            book__service__pb2.UpdateBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/bookservice.BookService/DeleteBook',
            book__service__pb2.DeleteBookRequest.SerializeToString,
            book__service__pb2.DeleteBookResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
