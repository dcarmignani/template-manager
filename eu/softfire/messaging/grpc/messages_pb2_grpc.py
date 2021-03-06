# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import eu.softfire.tub.messaging.grpc.messages_pb2 as messages__pb2


class RegistrationServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.register = channel.unary_unary(
        '/RegistrationService/register',
        request_serializer=messages__pb2.RegisterMessage.SerializeToString,
        response_deserializer=messages__pb2.ResponseMessage.FromString,
        )
    self.unregister = channel.unary_unary(
        '/RegistrationService/unregister',
        request_serializer=messages__pb2.UnregisterMessage.SerializeToString,
        response_deserializer=messages__pb2.ResponseMessage.FromString,
        )


class RegistrationServiceServicer(object):

  def register(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unregister(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RegistrationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'register': grpc.unary_unary_rpc_method_handler(
          servicer.register,
          request_deserializer=messages__pb2.RegisterMessage.FromString,
          response_serializer=messages__pb2.ResponseMessage.SerializeToString,
      ),
      'unregister': grpc.unary_unary_rpc_method_handler(
          servicer.unregister,
          request_deserializer=messages__pb2.UnregisterMessage.FromString,
          response_serializer=messages__pb2.ResponseMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RegistrationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ManagerAgentStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.execute = channel.unary_unary(
        '/ManagerAgent/execute',
        request_serializer=messages__pb2.RequestMessage.SerializeToString,
        response_deserializer=messages__pb2.ResponseMessage.FromString,
        )


class ManagerAgentServicer(object):

  def execute(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ManagerAgentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'execute': grpc.unary_unary_rpc_method_handler(
          servicer.execute,
          request_deserializer=messages__pb2.RequestMessage.FromString,
          response_serializer=messages__pb2.ResponseMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ManagerAgent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
