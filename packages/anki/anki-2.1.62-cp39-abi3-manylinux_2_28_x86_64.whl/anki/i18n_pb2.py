# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki/i18n.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki import generic_pb2 as anki_dot_generic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61nki/i18n.proto\x12\tanki.i18n\x1a\x12\x61nki/generic.proto\"\xcb\x01\n\x16TranslateStringRequest\x12\x14\n\x0cmodule_index\x18\x01 \x01(\r\x12\x15\n\rmessage_index\x18\x02 \x01(\r\x12\x39\n\x04\x61rgs\x18\x03 \x03(\x0b\x32+.anki.i18n.TranslateStringRequest.ArgsEntry\x1aI\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.anki.i18n.TranslateArgValue:\x02\x38\x01\"=\n\x11TranslateArgValue\x12\r\n\x03str\x18\x01 \x01(\tH\x00\x12\x10\n\x06number\x18\x02 \x01(\x01H\x00\x42\x07\n\x05value\"\x9e\x01\n\x15\x46ormatTimespanRequest\x12\x0f\n\x07seconds\x18\x01 \x01(\x02\x12\x39\n\x07\x63ontext\x18\x02 \x01(\x0e\x32(.anki.i18n.FormatTimespanRequest.Context\"9\n\x07\x43ontext\x12\x0b\n\x07PRECISE\x10\x00\x12\x12\n\x0e\x41NSWER_BUTTONS\x10\x01\x12\r\n\tINTERVALS\x10\x02\"\'\n\x14I18nResourcesRequest\x12\x0f\n\x07modules\x18\x01 \x03(\t2\xe9\x01\n\x0bI18nService\x12J\n\x0fTranslateString\x12!.anki.i18n.TranslateStringRequest\x1a\x14.anki.generic.String\x12H\n\x0e\x46ormatTimespan\x12 .anki.i18n.FormatTimespanRequest\x1a\x14.anki.generic.String\x12\x44\n\rI18nResources\x12\x1f.anki.i18n.I18nResourcesRequest\x1a\x12.anki.generic.JsonB\x02P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anki.i18n_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _TRANSLATESTRINGREQUEST_ARGSENTRY._options = None
  _TRANSLATESTRINGREQUEST_ARGSENTRY._serialized_options = b'8\001'
  _TRANSLATESTRINGREQUEST._serialized_start=51
  _TRANSLATESTRINGREQUEST._serialized_end=254
  _TRANSLATESTRINGREQUEST_ARGSENTRY._serialized_start=181
  _TRANSLATESTRINGREQUEST_ARGSENTRY._serialized_end=254
  _TRANSLATEARGVALUE._serialized_start=256
  _TRANSLATEARGVALUE._serialized_end=317
  _FORMATTIMESPANREQUEST._serialized_start=320
  _FORMATTIMESPANREQUEST._serialized_end=478
  _FORMATTIMESPANREQUEST_CONTEXT._serialized_start=421
  _FORMATTIMESPANREQUEST_CONTEXT._serialized_end=478
  _I18NRESOURCESREQUEST._serialized_start=480
  _I18NRESOURCESREQUEST._serialized_end=519
  _I18NSERVICE._serialized_start=522
  _I18NSERVICE._serialized_end=755
# @@protoc_insertion_point(module_scope)
