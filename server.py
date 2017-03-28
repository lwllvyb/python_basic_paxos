# -*- coding:utf-8 -*-

"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import basic_paxos_pb2
import basic_paxos_pb2_grpc
import xmlrpclib
import socket
import threading
import os
import socket
import sys

def PortIsInUse(ip, port):
    '''
    detect if the socket(ip:port) in use.
    '''
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        return True
    except:
        return False

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Propoer(object):
    '''
    class proposer
    '''

    def __init__(self):
        self.rpc_port = 8000
        self.rpc_ip = "localhost"

        # Proposer
        self.last_prepare_b = 0
        self.maxab = 0
        self.g_qrm_nums = 2
        self.current_b = 0
        self.value = None
        self.accept_value = None
        # acceptor
        self.pb = 0
        self.ab = 0
        self.av = None

        # Record all the servers' info
        self.servers = []

        self.EOK = 0
        self.EREJECT = 1

    def start_prepare(self, value):
        '''
        Proposer to start prepare
        '''
        self.current_b = self.last_prepare_b + 1
        self.value = value

        for server in self.servers:
            print("%s--" % server)
            for i in range(3):
                try:
                    print "[%s] server [%s]" % (i, server)
                    server["prepare_result"] = server[
                        'server'].acceptor_prepare(self.current_b)
                    break

                except socket.error:
                    server['server'] = xmlrpclib.ServerProxy(
                        "http://%s/" % server['ipport'], allow_none=True)

    def prepare_response(self):
        '''
        Handle prepare response
        '''
        print "1"
        prepare_oks = len(filter(lambda x: x['prepare_result'] and x[
                          'prepare_result'][0] == self.EOK, self.servers))
        if prepare_oks >= self.g_qrm_nums:
            for server in self.servers:
                if server["prepare_result"] is None:
                    continue
                if server["prepare_result"][0] != self.EOK:
                    continue
                print("2 - %s" % server)
                ab = server["prepare_result"][1]
                av = server["prepare_result"][2]
                if ab > self.maxab and av is not None:
                    print "3"
                    self.maxab = ab
                    self.accept_value = self.av
                    server["accept_result"] =\
                        server["server"].acceptor_accept(self.current_b,
                                                         self.accept_value)
                else:
                    print "4"
                    self.accept_value = self.value
                    server["accept_result"] =\
                        server["server"].acceptor_accept(self.current_b,
                                                         self.accept_value)
                    print("4....")
        else:
            print "prepare fail! prepare response [%s/%s], " % (prepare_oks, self.g_qrm_nums)

    def accept_response(self):
        '''
        Handle acceptor response
        '''

        accept_oks = []
        for server in self.servers:
            if server["accept_result"] is not None and server["accept_result"] == 0:
                accept_oks.append(server)

        if len(accept_oks) >= self.g_qrm_nums:
            print("%s %s is accept by quroms!"
                  % (self.value, self.accept_value))

    def start_paxos(self, value):
        '''
        Start paxos
        '''
        state = "StartProposol"
        retry_time = 0

        while state in self.state_table:
            if state == "StartProposol":
                retry_time += 1
            elif state == "FinishProposol":
                print("Finish proposol!")
                break
            elif retry_time >= 3:
                print("Error: retry time is %s" % retry_time)
                break

            state = self.basic_paxos_state_machine(state)
            print ("Next state [%s]" % state)

    def make_state_table(self):
        self.state_table = [
            "StartProposol",
            "PrepareRequest",
            "HandlePrepareResponse",
            "AcceptorPrepare",
            "HandleAcceptorResponse",
            "FinishProposol",
        ]

    def basic_paxos_state_machine(state):
        '''
        simple state machine for basic paxos
        '''
        if state == "StartProposol":
            ret = self.start_prepare(self.value)
            if ret == G_EOK:
                return "PrepareRequest"
        elif state == "PrepareRequest":
            ret = self.prepare_request(self.vote_id)
            if ret == G_EOK:
                return "HandlePrepareResponse"
        elif state == "HandlePrepareResponse":
            ret = self.handle_prepare_response()
            if ret == G_EOK:
                return "AcceptorPrepare"
        elif state == "AcceptorPrepare":
            ret = self.acceptor_prepare(self.vote_id, self.value)
            if ret == G_EOK:
                return "HandleAcceptorResponse"
        elif state == "HandleAcceptorResponse":
            ret = self.handle_prepare_response()
            if ret == G_EOK:
                return "FinishProposol"
        return "StartProposol"


G_EOK = 0
G_EREJECT = 1


class Acceptor(object):

    def __init__(self):
        self.prepare_accepted_vote_id = 0
        self.accepted_vote_id = 0
        self.accepted_value = None

    def acceptor_prepare(self, vote_id):

        if vote_id >= self.prepare_accepted_vote_id:
            self.prepare_accepted_vote_id = vote_id

            return (G_EOK, self.accepted_vote_id, self.accepted_value)
        else:
            return (G_EREJECT, 0, "")

    def acceptor_accept(self, vote_id, value):
        if vote_id >= self.prepare_accepted_vote_id:
            self.accepted_vote_id = vote_id
            self.accepted_value = value
            print "acceptor_accept:%s" % G_EOK
            return G_EOK
        else:
            return G_EREJECT


# 创建 acceptor
g_acceptor = Acceptor()


class BasicPaxosServicer(basic_paxos_pb2_grpc.BasicPaxosServicer):

    def acceptor_prepare(self, request, context):
        '''
        Accept prepare
        '''

        print("request:%s" % request)
        ret = g_acceptor.acceptor_prepare(request.vote_id)
        print("ret:%s" % str(ret))
        return basic_paxos_pb2.AcceptorPrepareResponse(ret_code=ret[0],
                                                       accepted_vote_id=ret[1], accepted_value=ret[2])
        # return basic_paxos_pb2.AcceptorPrepareResponse(ret_code=G_EOK,
        # accepted_vote_id=G_AB, accepted_value=G_AV)

    def acceptor_accept(self, request, context):
        '''
        acceptor handle accept
        '''

        print("request:%s" % request)
        ret = g_acceptor.acceptor_accept(request.vote_id, request.value)
        print("ret:%s" % str(ret))
        return basic_paxos_pb2.AcceptorAcceptResponse(ret_code=ret)


def start_server(port=50051):
    '''
    start_server
    '''
    BasicPaxos_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    basic_paxos_pb2_grpc.add_BasicPaxosServicer_to_server(
        BasicPaxosServicer(), BasicPaxos_server)
    BasicPaxos_server.add_insecure_port('[::]:%s' % port)
    BasicPaxos_server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        BasicPaxos_server.stop(0)


if __name__ == '__main__':
    port = 50051
    port_max_num = port + 10
    while PortIsInUse("127.0.0.1", port):
        if port >= port_max_num:
            print("prot is %s, exit script!" % port)
            sys.exit(0)
        port += 1
    print("Port [%s]" % port)
    start_server(port)
