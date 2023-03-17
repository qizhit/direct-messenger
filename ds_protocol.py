"""
transfer the json data of server response
"""
# ds_protocol.py

# Starter code for assignment 3 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950

import json
from collections import namedtuple


def msg_join(username, password):
    """tranfer the join message to server style"""
    msg = {"join": {"username": username, "password": password, "token": ""}}
    return json.dumps(msg)


def server_post(token, message, timestamp):
    """transfer the post message to server style"""
    msg = {"token": token, "post": {"entry": message, "timestamp": timestamp}}
    return json.dumps(msg)


def server_bio(token, bio, timestamp):
    """transfer the bio message to server style"""
    msg = {"token": token, "bio": {"entry": bio, "timestamp": timestamp}}
    return json.dumps(msg)


# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['type_status', 'token'])


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
        if 'token' in response.keys():
            token = json_obj['response']['token']

        return DataTuple(type_status, token)

    except json.JSONDecodeError:
        print("Json cannot be decoded.")
