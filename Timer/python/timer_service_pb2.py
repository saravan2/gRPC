# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timer_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13timer_service.proto\x12\x05timer\" \n\x0cTimerRequest\x12\x10\n\x08\x64uration\x18\x01 \x01(\x05\" \n\rTimerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2N\n\x0cTimerService\x12>\n\rRegisterTimer\x12\x13.timer.TimerRequest\x1a\x14.timer.TimerResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'timer_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMERREQUEST']._serialized_start=30
  _globals['_TIMERREQUEST']._serialized_end=62
  _globals['_TIMERRESPONSE']._serialized_start=64
  _globals['_TIMERRESPONSE']._serialized_end=96
  _globals['_TIMERSERVICE']._serialized_start=98
  _globals['_TIMERSERVICE']._serialized_end=176
# @@protoc_insertion_point(module_scope)
