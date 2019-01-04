# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_desc.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='module_desc.proto',
    package='paddle_hub',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x11module_desc.proto\x12\npaddle_hub\"\x19\n\tInputDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\nOutputDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xb3\x01\n\nModuleDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\ninput_desc\x18\x02 \x03(\x0b\x32\x15.paddle_hub.InputDesc\x12+\n\x0boutput_desc\x18\x03 \x03(\x0b\x32\x16.paddle_hub.OutputDesc\x12\x11\n\tsignature\x18\x04 \x01(\t\x12\x14\n\x0creturn_numpy\x18\x05 \x01(\x08\x12\x16\n\x0e\x63ontain_assets\x18\x06 \x01(\x08\x42\x02H\x03\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INPUTDESC = _descriptor.Descriptor(
    name='InputDesc',
    full_name='paddle_hub.InputDesc',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='paddle_hub.InputDesc.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=33,
    serialized_end=58, )

_OUTPUTDESC = _descriptor.Descriptor(
    name='OutputDesc',
    full_name='paddle_hub.OutputDesc',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='paddle_hub.OutputDesc.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=60,
    serialized_end=86, )

_MODULEDESC = _descriptor.Descriptor(
    name='ModuleDesc',
    full_name='paddle_hub.ModuleDesc',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='paddle_hub.ModuleDesc.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='input_desc',
            full_name='paddle_hub.ModuleDesc.input_desc',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='output_desc',
            full_name='paddle_hub.ModuleDesc.output_desc',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='signature',
            full_name='paddle_hub.ModuleDesc.signature',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='return_numpy',
            full_name='paddle_hub.ModuleDesc.return_numpy',
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='contain_assets',
            full_name='paddle_hub.ModuleDesc.contain_assets',
            index=5,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=89,
    serialized_end=268, )

_MODULEDESC.fields_by_name['input_desc'].message_type = _INPUTDESC
_MODULEDESC.fields_by_name['output_desc'].message_type = _OUTPUTDESC
DESCRIPTOR.message_types_by_name['InputDesc'] = _INPUTDESC
DESCRIPTOR.message_types_by_name['OutputDesc'] = _OUTPUTDESC
DESCRIPTOR.message_types_by_name['ModuleDesc'] = _MODULEDESC

InputDesc = _reflection.GeneratedProtocolMessageType(
    'InputDesc',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_INPUTDESC,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.InputDesc)
    ))
_sym_db.RegisterMessage(InputDesc)

OutputDesc = _reflection.GeneratedProtocolMessageType(
    'OutputDesc',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_OUTPUTDESC,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.OutputDesc)
    ))
_sym_db.RegisterMessage(OutputDesc)

ModuleDesc = _reflection.GeneratedProtocolMessageType(
    'ModuleDesc',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_MODULEDESC,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.ModuleDesc)
    ))
_sym_db.RegisterMessage(ModuleDesc)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('H\003'))
# @@protoc_insertion_point(module_scope)
