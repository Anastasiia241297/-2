# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: score.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'score.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bscore.proto\"\x1d\n\x0cScoreRequest\x12\r\n\x05login\x18\x01 \x01(\t\"\x1e\n\rScoreResponse\x12\r\n\x05score\x18\x01 \x01(\x02\x32\x39\n\x0cScoreService\x12)\n\x08GetScore\x12\r.ScoreRequest\x1a\x0e.ScoreResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'score_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SCOREREQUEST']._serialized_start=15
  _globals['_SCOREREQUEST']._serialized_end=44
  _globals['_SCORERESPONSE']._serialized_start=46
  _globals['_SCORERESPONSE']._serialized_end=76
  _globals['_SCORESERVICE']._serialized_start=78
  _globals['_SCORESERVICE']._serialized_end=135
# @@protoc_insertion_point(module_scope)
