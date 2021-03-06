# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crud.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crud.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ncrud.proto\"U\n\x0e\x63reate_student\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64ob\x18\x02 \x01(\t\x12\x12\n\nstudent_id\x18\x03 \x01(\x05\x12\x14\n\x0cmobilenumber\x18\x04 \x01(\t\"U\n\x0eupdate_student\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64ob\x18\x02 \x01(\t\x12\x12\n\nstudent_id\x18\x03 \x01(\x05\x12\x14\n\x0cmobilenumber\x18\x04 \x01(\t\"$\n\x0e\x64\x65lete_student\x12\x12\n\nstudent_id\x18\x01 \x01(\x05\"T\n\rfetch_student\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64ob\x18\x02 \x01(\t\x12\x12\n\nstudent_id\x18\x03 \x01(\x05\x12\x14\n\x0cmobilenumber\x18\x04 \x01(\t\"4\n\x11\x66\x65tch_student_all\x12\x1f\n\x07\x61lldata\x18\x01 \x03(\x0b\x32\x0e.fetch_student\"\x1e\n\x0fsuccess_message\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x06\n\x04Null2\xe4\x01\n\x0f\x63rud_operations\x12,\n\rfetchStudentD\x12\x05.Null\x1a\x12.fetch_student_all\"\x00\x12\x35\n\x0e\x63reateStudentD\x12\x0f.create_student\x1a\x10.success_message\"\x00\x12\x35\n\x0eupdateStudentD\x12\x0f.update_student\x1a\x10.success_message\"\x00\x12\x35\n\x0e\x64\x65leteStudentD\x12\x0f.delete_student\x1a\x10.success_message\"\x00\x62\x06proto3'
)




_CREATE_STUDENT = _descriptor.Descriptor(
  name='create_student',
  full_name='create_student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='create_student.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dob', full_name='create_student.dob', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_id', full_name='create_student.student_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='create_student.mobilenumber', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=99,
)


_UPDATE_STUDENT = _descriptor.Descriptor(
  name='update_student',
  full_name='update_student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='update_student.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dob', full_name='update_student.dob', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_id', full_name='update_student.student_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='update_student.mobilenumber', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=186,
)


_DELETE_STUDENT = _descriptor.Descriptor(
  name='delete_student',
  full_name='delete_student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='student_id', full_name='delete_student.student_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=224,
)


_FETCH_STUDENT = _descriptor.Descriptor(
  name='fetch_student',
  full_name='fetch_student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fetch_student.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dob', full_name='fetch_student.dob', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_id', full_name='fetch_student.student_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='fetch_student.mobilenumber', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=310,
)


_FETCH_STUDENT_ALL = _descriptor.Descriptor(
  name='fetch_student_all',
  full_name='fetch_student_all',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alldata', full_name='fetch_student_all.alldata', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=364,
)


_SUCCESS_MESSAGE = _descriptor.Descriptor(
  name='success_message',
  full_name='success_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='success_message.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=396,
)


_NULL = _descriptor.Descriptor(
  name='Null',
  full_name='Null',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=404,
)

_FETCH_STUDENT_ALL.fields_by_name['alldata'].message_type = _FETCH_STUDENT
DESCRIPTOR.message_types_by_name['create_student'] = _CREATE_STUDENT
DESCRIPTOR.message_types_by_name['update_student'] = _UPDATE_STUDENT
DESCRIPTOR.message_types_by_name['delete_student'] = _DELETE_STUDENT
DESCRIPTOR.message_types_by_name['fetch_student'] = _FETCH_STUDENT
DESCRIPTOR.message_types_by_name['fetch_student_all'] = _FETCH_STUDENT_ALL
DESCRIPTOR.message_types_by_name['success_message'] = _SUCCESS_MESSAGE
DESCRIPTOR.message_types_by_name['Null'] = _NULL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

create_student = _reflection.GeneratedProtocolMessageType('create_student', (_message.Message,), {
  'DESCRIPTOR' : _CREATE_STUDENT,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:create_student)
  })
_sym_db.RegisterMessage(create_student)

update_student = _reflection.GeneratedProtocolMessageType('update_student', (_message.Message,), {
  'DESCRIPTOR' : _UPDATE_STUDENT,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:update_student)
  })
_sym_db.RegisterMessage(update_student)

delete_student = _reflection.GeneratedProtocolMessageType('delete_student', (_message.Message,), {
  'DESCRIPTOR' : _DELETE_STUDENT,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:delete_student)
  })
_sym_db.RegisterMessage(delete_student)

fetch_student = _reflection.GeneratedProtocolMessageType('fetch_student', (_message.Message,), {
  'DESCRIPTOR' : _FETCH_STUDENT,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:fetch_student)
  })
_sym_db.RegisterMessage(fetch_student)

fetch_student_all = _reflection.GeneratedProtocolMessageType('fetch_student_all', (_message.Message,), {
  'DESCRIPTOR' : _FETCH_STUDENT_ALL,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:fetch_student_all)
  })
_sym_db.RegisterMessage(fetch_student_all)

success_message = _reflection.GeneratedProtocolMessageType('success_message', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESS_MESSAGE,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:success_message)
  })
_sym_db.RegisterMessage(success_message)

Null = _reflection.GeneratedProtocolMessageType('Null', (_message.Message,), {
  'DESCRIPTOR' : _NULL,
  '__module__' : 'crud_pb2'
  # @@protoc_insertion_point(class_scope:Null)
  })
_sym_db.RegisterMessage(Null)



_CRUD_OPERATIONS = _descriptor.ServiceDescriptor(
  name='crud_operations',
  full_name='crud_operations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=407,
  serialized_end=635,
  methods=[
  _descriptor.MethodDescriptor(
    name='fetchStudentD',
    full_name='crud_operations.fetchStudentD',
    index=0,
    containing_service=None,
    input_type=_NULL,
    output_type=_FETCH_STUDENT_ALL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='createStudentD',
    full_name='crud_operations.createStudentD',
    index=1,
    containing_service=None,
    input_type=_CREATE_STUDENT,
    output_type=_SUCCESS_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateStudentD',
    full_name='crud_operations.updateStudentD',
    index=2,
    containing_service=None,
    input_type=_UPDATE_STUDENT,
    output_type=_SUCCESS_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteStudentD',
    full_name='crud_operations.deleteStudentD',
    index=3,
    containing_service=None,
    input_type=_DELETE_STUDENT,
    output_type=_SUCCESS_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRUD_OPERATIONS)

DESCRIPTOR.services_by_name['crud_operations'] = _CRUD_OPERATIONS

# @@protoc_insertion_point(module_scope)
