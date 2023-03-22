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

# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['type_status', 'token', 'messages'])


# Sending of direct message was successful
# {"response": {"type": "ok", "message": "Direct message sent"}}

# Response to request for **`all`** and **`new`** messages.
# Timestamp is time in seconds of when the message was originally sent.
# {"response": {"type": "ok", "messages":
# [{"message":"Hello", "from":"xxx", "timestamp":"1603167689.3928561"}]}}


def extract_json(json_msg: str):
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

        return DataTuple(type_status, token, messages)

    except json.JSONDecodeError:
        print("Json cannot be decoded.")
        return None
