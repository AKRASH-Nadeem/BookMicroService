# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: book_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'book_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62ook_service.proto\x12\x0b\x62ookservice\"`\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x18\n\x10publication_year\x18\x05 \x01(\x05\"1\n\x0e\x41\x64\x64\x42ookRequest\x12\x1f\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x11.bookservice.Book\"B\n\x0f\x41\x64\x64\x42ookResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x1f\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x11.bookservice.Book\"\x1c\n\x0eGetBookRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"2\n\x0fGetBookResponse\x12\x1f\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x11.bookservice.Book\"4\n\x11UpdateBookRequest\x12\x1f\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x11.bookservice.Book\"E\n\x12UpdateBookResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x1f\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x11.bookservice.Book\"\x1f\n\x11\x44\x65leteBookRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"$\n\x12\x44\x65leteBookResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xb7\x02\n\x0b\x42ookService\x12\x44\n\x07\x41\x64\x64\x42ook\x12\x1b.bookservice.AddBookRequest\x1a\x1c.bookservice.AddBookResponse\x12\x44\n\x07GetBook\x12\x1b.bookservice.GetBookRequest\x1a\x1c.bookservice.GetBookResponse\x12M\n\nUpdateBook\x12\x1e.bookservice.UpdateBookRequest\x1a\x1f.bookservice.UpdateBookResponse\x12M\n\nDeleteBook\x12\x1e.bookservice.DeleteBookRequest\x1a\x1f.bookservice.DeleteBookResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOK']._serialized_start=35
  _globals['_BOOK']._serialized_end=131
  _globals['_ADDBOOKREQUEST']._serialized_start=133
  _globals['_ADDBOOKREQUEST']._serialized_end=182
  _globals['_ADDBOOKRESPONSE']._serialized_start=184
  _globals['_ADDBOOKRESPONSE']._serialized_end=250
  _globals['_GETBOOKREQUEST']._serialized_start=252
  _globals['_GETBOOKREQUEST']._serialized_end=280
  _globals['_GETBOOKRESPONSE']._serialized_start=282
  _globals['_GETBOOKRESPONSE']._serialized_end=332
  _globals['_UPDATEBOOKREQUEST']._serialized_start=334
  _globals['_UPDATEBOOKREQUEST']._serialized_end=386
  _globals['_UPDATEBOOKRESPONSE']._serialized_start=388
  _globals['_UPDATEBOOKRESPONSE']._serialized_end=457
  _globals['_DELETEBOOKREQUEST']._serialized_start=459
  _globals['_DELETEBOOKREQUEST']._serialized_end=490
  _globals['_DELETEBOOKRESPONSE']._serialized_start=492
  _globals['_DELETEBOOKRESPONSE']._serialized_end=528
  _globals['_BOOKSERVICE']._serialized_start=531
  _globals['_BOOKSERVICE']._serialized_end=842
# @@protoc_insertion_point(module_scope)
