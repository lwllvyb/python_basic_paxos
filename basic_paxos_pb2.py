# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basic_paxos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basic_paxos.proto',
  package='basicpaxos',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x62\x61sic_paxos.proto\x12\nbasicpaxos\")\n\x16\x41\x63\x63\x65ptorPrepareRequest\x12\x0f\n\x07vote_id\x18\x01 \x01(\x05\"]\n\x17\x41\x63\x63\x65ptorPrepareResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x18\n\x10\x61\x63\x63\x65pted_vote_id\x18\x02 \x01(\x05\x12\x16\n\x0e\x61\x63\x63\x65pted_value\x18\x03 \x01(\t\"7\n\x15\x41\x63\x63\x65ptorAcceptRequest\x12\x0f\n\x07vote_id\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"*\n\x16\x41\x63\x63\x65ptorAcceptResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x32\xc7\x01\n\nBasicPaxos\x12]\n\x10\x61\x63\x63\x65ptor_prepare\x12\".basicpaxos.AcceptorPrepareRequest\x1a#.basicpaxos.AcceptorPrepareResponse\"\x00\x12Z\n\x0f\x61\x63\x63\x65ptor_accept\x12!.basicpaxos.AcceptorAcceptRequest\x1a\".basicpaxos.AcceptorAcceptResponse\"\x00\x42\x36\n\x1cio.grpc.examples.basic_paxosB\x0f\x42\x61sicPaxosProtoP\x01\xa2\x02\x02\x42Pb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACCEPTORPREPAREREQUEST = _descriptor.Descriptor(
  name='AcceptorPrepareRequest',
  full_name='basicpaxos.AcceptorPrepareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote_id', full_name='basicpaxos.AcceptorPrepareRequest.vote_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=74,
)


_ACCEPTORPREPARERESPONSE = _descriptor.Descriptor(
  name='AcceptorPrepareResponse',
  full_name='basicpaxos.AcceptorPrepareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='basicpaxos.AcceptorPrepareResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accepted_vote_id', full_name='basicpaxos.AcceptorPrepareResponse.accepted_vote_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accepted_value', full_name='basicpaxos.AcceptorPrepareResponse.accepted_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=169,
)


_ACCEPTORACCEPTREQUEST = _descriptor.Descriptor(
  name='AcceptorAcceptRequest',
  full_name='basicpaxos.AcceptorAcceptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote_id', full_name='basicpaxos.AcceptorAcceptRequest.vote_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='basicpaxos.AcceptorAcceptRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=226,
)


_ACCEPTORACCEPTRESPONSE = _descriptor.Descriptor(
  name='AcceptorAcceptResponse',
  full_name='basicpaxos.AcceptorAcceptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='basicpaxos.AcceptorAcceptResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=270,
)

DESCRIPTOR.message_types_by_name['AcceptorPrepareRequest'] = _ACCEPTORPREPAREREQUEST
DESCRIPTOR.message_types_by_name['AcceptorPrepareResponse'] = _ACCEPTORPREPARERESPONSE
DESCRIPTOR.message_types_by_name['AcceptorAcceptRequest'] = _ACCEPTORACCEPTREQUEST
DESCRIPTOR.message_types_by_name['AcceptorAcceptResponse'] = _ACCEPTORACCEPTRESPONSE

AcceptorPrepareRequest = _reflection.GeneratedProtocolMessageType('AcceptorPrepareRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTORPREPAREREQUEST,
  __module__ = 'basic_paxos_pb2'
  # @@protoc_insertion_point(class_scope:basicpaxos.AcceptorPrepareRequest)
  ))
_sym_db.RegisterMessage(AcceptorPrepareRequest)

AcceptorPrepareResponse = _reflection.GeneratedProtocolMessageType('AcceptorPrepareResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTORPREPARERESPONSE,
  __module__ = 'basic_paxos_pb2'
  # @@protoc_insertion_point(class_scope:basicpaxos.AcceptorPrepareResponse)
  ))
_sym_db.RegisterMessage(AcceptorPrepareResponse)

AcceptorAcceptRequest = _reflection.GeneratedProtocolMessageType('AcceptorAcceptRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTORACCEPTREQUEST,
  __module__ = 'basic_paxos_pb2'
  # @@protoc_insertion_point(class_scope:basicpaxos.AcceptorAcceptRequest)
  ))
_sym_db.RegisterMessage(AcceptorAcceptRequest)

AcceptorAcceptResponse = _reflection.GeneratedProtocolMessageType('AcceptorAcceptResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTORACCEPTRESPONSE,
  __module__ = 'basic_paxos_pb2'
  # @@protoc_insertion_point(class_scope:basicpaxos.AcceptorAcceptResponse)
  ))
_sym_db.RegisterMessage(AcceptorAcceptResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034io.grpc.examples.basic_paxosB\017BasicPaxosProtoP\001\242\002\002BP'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class BasicPaxosStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.acceptor_prepare = channel.unary_unary(
          '/basicpaxos.BasicPaxos/acceptor_prepare',
          request_serializer=AcceptorPrepareRequest.SerializeToString,
          response_deserializer=AcceptorPrepareResponse.FromString,
          )
      self.acceptor_accept = channel.unary_unary(
          '/basicpaxos.BasicPaxos/acceptor_accept',
          request_serializer=AcceptorAcceptRequest.SerializeToString,
          response_deserializer=AcceptorAcceptResponse.FromString,
          )


  class BasicPaxosServicer(object):
    """The greeting service definition.
    """

    def acceptor_prepare(self, request, context):
      """Sends a greeting
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def acceptor_accept(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_BasicPaxosServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'acceptor_prepare': grpc.unary_unary_rpc_method_handler(
            servicer.acceptor_prepare,
            request_deserializer=AcceptorPrepareRequest.FromString,
            response_serializer=AcceptorPrepareResponse.SerializeToString,
        ),
        'acceptor_accept': grpc.unary_unary_rpc_method_handler(
            servicer.acceptor_accept,
            request_deserializer=AcceptorAcceptRequest.FromString,
            response_serializer=AcceptorAcceptResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'basicpaxos.BasicPaxos', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaBasicPaxosServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The greeting service definition.
    """
    def acceptor_prepare(self, request, context):
      """Sends a greeting
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def acceptor_accept(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaBasicPaxosStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The greeting service definition.
    """
    def acceptor_prepare(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Sends a greeting
      """
      raise NotImplementedError()
    acceptor_prepare.future = None
    def acceptor_accept(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    acceptor_accept.future = None


  def beta_create_BasicPaxos_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('basicpaxos.BasicPaxos', 'acceptor_accept'): AcceptorAcceptRequest.FromString,
      ('basicpaxos.BasicPaxos', 'acceptor_prepare'): AcceptorPrepareRequest.FromString,
    }
    response_serializers = {
      ('basicpaxos.BasicPaxos', 'acceptor_accept'): AcceptorAcceptResponse.SerializeToString,
      ('basicpaxos.BasicPaxos', 'acceptor_prepare'): AcceptorPrepareResponse.SerializeToString,
    }
    method_implementations = {
      ('basicpaxos.BasicPaxos', 'acceptor_accept'): face_utilities.unary_unary_inline(servicer.acceptor_accept),
      ('basicpaxos.BasicPaxos', 'acceptor_prepare'): face_utilities.unary_unary_inline(servicer.acceptor_prepare),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_BasicPaxos_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('basicpaxos.BasicPaxos', 'acceptor_accept'): AcceptorAcceptRequest.SerializeToString,
      ('basicpaxos.BasicPaxos', 'acceptor_prepare'): AcceptorPrepareRequest.SerializeToString,
    }
    response_deserializers = {
      ('basicpaxos.BasicPaxos', 'acceptor_accept'): AcceptorAcceptResponse.FromString,
      ('basicpaxos.BasicPaxos', 'acceptor_prepare'): AcceptorPrepareResponse.FromString,
    }
    cardinalities = {
      'acceptor_accept': cardinality.Cardinality.UNARY_UNARY,
      'acceptor_prepare': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'basicpaxos.BasicPaxos', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)