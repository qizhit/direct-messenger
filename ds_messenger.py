"""
ds_messenger.py
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

import socket
import copy
import json
import time
from collections import namedtuple

DataTuple = namedtuple('DataTuple', ['type_status', 'token', 'messages'])


def extract_json(json_msg: str) -> DataTuple:
    """
    Call the json.loads function on a json string and
    convert it to a DataTuple object

    """
    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        type_status = json_obj['response']['type']
        token = ''
        messages = ''
        if 'token' in response.keys():
            token = json_obj['response']['token']
        if 'message' in response.keys():
            messages = json_obj['response']['message']
        if 'messages' in response.keys():
            messages = json_obj['response']['messages']

        return DataTuple(type_status=type_status,
                         token=token, messages=messages)

    except json.JSONDecodeError:
        print("Json cannot be decoded.")


class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.send_1 = None
        self.recv_1 = None

    def send(self, message: str, recipient: str) -> bool:
        """return true if message successfully sent, false if send failed."""
        try:
            timestamp = time.time()
            msg = dict(token=self.token,
                       directmessage={"entry": message, "recipient": recipient,
                                      "timestamp": timestamp})
            msg = json.dumps(msg)
            self.send_1.write(msg + '\r\n')
            self.send_1.flush()
            resp = self.recv_1.readline()
            resp_np = extract_json(resp)

            if resp_np.type_status == 'error':
                return False

            print(f"{resp_np.messages}")
            return True
        except AttributeError:
            return False

    def retrieve_new(self) -> list:
        """return a list of DirectMessage objects containing all new msgs"""
        msg = {"token": self.token, "directmessage": "new"}
        msg = json.dumps(msg)

        self.send_1.write(msg + '\r\n')
        self.send_1.flush()
        resp = self.recv_1.readline()
        resp_np = extract_json(resp)

        directmessage = DirectMessage()
        direct_messages = []
        for mes in resp_np.messages:
            directmessage.recipient = mes['from']
            directmessage.message = mes['message']
            directmessage.timestamp = mes['timestamp']
            direct_messages.append(copy.deepcopy(directmessage))

        return direct_messages

    def retrieve_all(self) -> list:
        """return a list of DirectMessage objects containing all messages"""
        msg = {"token": self.token, "directmessage": "all"}
        msg = json.dumps(msg)

        self.send_1.write(msg + '\r\n')
        self.send_1.flush()
        resp = self.recv_1.readline()
        resp_np = extract_json(resp)

        directmessage = DirectMessage()
        direct_messages = []
        for mes in resp_np.messages:
            directmessage.recipient = mes['from']
            directmessage.message = mes['message']
            directmessage.timestamp = mes['timestamp']
            direct_messages.append(copy.deepcopy(directmessage))

        return direct_messages

    def connect(self):
        """
        connect to the server and get the token
        """
        port = 3021
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((self.dsuserver, port))

                join_msg = {"join": {"username": self.username,
                                     "password": self.password, "token": ""}}
                join_msg = json.dumps(join_msg)

                send_token = client.makefile('w')
                recv_token = client.makefile('r')
                send_token.write(join_msg + '\r\n')
                send_token.flush()
                resp = recv_token.readline()
                resp_np = extract_json(resp)

                if resp_np.type_status != 'ok':
                    return False

                self.token = resp_np.token

                self.send_1 = client.makefile('w')
                self.recv_1 = client.makefile('r')

                return True

        except (ConnectionRefusedError, socket.gaierror, TypeError, NameError):
            return False
