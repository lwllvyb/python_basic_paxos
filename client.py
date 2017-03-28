# -*- coding:utf-8 -*-
'''
client
'''

from __future__ import print_function

import grpc

import basic_paxos_pb2
import basic_paxos_pb2_grpc

import functools
import socket
import sys


def log(fun):  # decorator
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print ('begin call: %s()' % fun.__name__)
        ret = fun(*args, **kw)
        print ('end   call: %s()' % fun.__name__)
        return ret
    return wrapper


def PortIsInUse(ip, port):
    '''
    detect if the socket(ip:port) in use.
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


class Proposer(object):

    def __init__(self):
        self.acceptor_sessions = {}  # store the session with acceptor
        # Proposer
        self.last_prepare_vote_id = 0
        self.maxab = 0
        self.g_qrm_nums = 2
        self.value = None
        self.accepted_value = None

        self.EOK = 0
        self.EREJECT = 1

    @log
    def start_prepare(self):
        self.current_vote_id = self.last_prepare_vote_id + 1
        return self.EOK

    @log
    def prepare_request(self):
        '''
        Proposer to start prepare
        '''
        # todo 修改为线程。与每个acceptor进行通信。由最后一个进行调用后续处理
        for port, session in self.acceptor_sessions.items():
            session["prepare_result"] = self.acceptor_prepare(session[
                                                              "session"])
            print("session :%s %s" % (port, session))
        return self.EOK

    @log
    def handle_prepare_response(self):
        '''
        Handle prepare response
        '''

        prepare_ok_num = 0
        for port, session in self.acceptor_sessions.items():
            if session["prepare_result"] is None:
                continue
            if session["prepare_result"][0] != self.EOK:
                continue
            print("session :%s %s" % (port, session))
            prepare_ok_num += 1
            accepted_vote_id = session["prepare_result"][1]
            accepted_value = session["prepare_result"][2]
            if accepted_vote_id > self.maxab and accepted_value is not None:

                self.maxab = accepted_vote_id
                self.accepted_value = accepted_value

            else:

                self.accepted_value = self.value

        if prepare_ok_num < self.g_qrm_nums:
            print (
                "prepare fail! prepare response [%s/%s], " % (prepare_ok_num, self.g_qrm_nums))
            return self.EREJECT
        return self.EOK

    @log
    def acceptor_request(self):
        for port, session in self.acceptor_sessions.items():
            if session["prepare_result"] is None:
                continue
            if session["prepare_result"][0] != self.EOK:
                continue

            session["accept_result"] = self.acceptor_accept(session["session"])
            print("session :%s %s" % (port, session))
        return self.EOK

    @log
    def handle_accept_response(self):
        '''
        Handle acceptor response
        '''

        acceptor_response_ok = 0
        for port, session in self.acceptor_sessions.items():
            print("%s %s" % (port, session))
            if session["accept_result"] is not None\
                and session["accept_result"][0] == self.EOK:
                acceptor_response_ok += 1

        if acceptor_response_ok >= self.g_qrm_nums:
            print("%s %s is accept by quroms!"
                  % (self.value, self.accepted_value))
            return self.EOK
        return self.EREJECT

    @log
    def connect_acceptor(self):

        for port in range(50051, 50061):
            if PortIsInUse("127.0.0.1", port):
                channel = grpc.insecure_channel('localhost:%s' % port)
                stub = basic_paxos_pb2_grpc.BasicPaxosStub(channel)
                self.acceptor_sessions[str(port)] = {"session": stub}

    @log
    def acceptor_prepare(self, stub):

        response = stub.acceptor_prepare(
            basic_paxos_pb2.AcceptorPrepareRequest(vote_id=self.current_vote_id))
        print("acceptor_prepare client received: %s" % (response.ret_code))
        return [response.ret_code, response.accepted_vote_id, response.accepted_value]

    @log
    def acceptor_accept(self, stub):
        response = stub.acceptor_accept(
            basic_paxos_pb2.AcceptorAcceptRequest(vote_id=self.current_vote_id, value=self.value))
        print("acceptor_accept client received again: %s" % response.ret_code)
        return [response.ret_code]

    @log
    def start_paxos(self, value):
        '''
        Start paxos
        '''
        state = "StartProposol"
        retry_time = 0
        self.vaue = value
        self.make_state_table()
        self.connect_acceptor()
        while state in self.state_table:
            if retry_time >= 3:
                print("Error: retry time is %s" % retry_time)
                break
            elif state == "StartProposol":
                retry_time += 1
                print("Retry time %s" % retry_time)
            elif state == "FinishProposol":
                print("Finish proposol!")
                break

            state = self.basic_paxos_state_machine(state)

            print ("Next state [%s]" % state)

    @log
    def make_state_table(self):
        self.state_table = [
            "StartProposol",
            "PrepareRequest",
            "HandlePrepareResponse",
            "AcceptorPrepare",
            "HandleAcceptorResponse",
            "FinishProposol",
        ]

    @log
    def basic_paxos_state_machine(self, state):
        '''
        simple state machine for basic paxos
        '''
        ret_state = "StartProposol"
        if state == "StartProposol":
            ret = self.start_prepare()
            if ret == self.EOK:
                ret_state = "PrepareRequest"
        elif state == "PrepareRequest":
            ret = self.prepare_request()
            if ret == self.EOK:
                ret_state = "HandlePrepareResponse"
        elif state == "HandlePrepareResponse":
            ret = self.handle_prepare_response()
            if ret == self.EOK:
                ret_state = "AcceptorPrepare"
        elif state == "AcceptorPrepare":
            ret = self.acceptor_request()
            if ret == self.EOK:
                ret_state = "HandleAcceptorResponse"
        elif state == "HandleAcceptorResponse":
            ret = self.handle_accept_response()
            if ret == self.EOK:
                ret_state = "FinishProposol"
        print("Pre state[%s], next state[%s]" % (state, ret_state))
        return ret_state


if __name__ == '__main__':
    p = Proposer()
    p.start_paxos("test")
