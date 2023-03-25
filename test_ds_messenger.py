"""
test ds_messenger.py
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

import unittest
import json
from collections import namedtuple
from ds_messenger import extract_json, DirectMessage, DirectMessenger


class TestDsmessenger(unittest.TestCase):
    """test ds_messenger"""
    def test_connect(self):
        """test connect()"""
        ds_messenger = DirectMessenger(dsuserver="168.235.86.102",
                                       username="nicaiwoshishei",
                                       password="buxiangshuohua")
        assert not ds_messenger.connect()

        ds_messenger = DirectMessenger(dsuserver="168.235.86.102",
                                       username="nicaiwoshishei",
                                       password="buxiangshuo")
        assert not ds_messenger.connect()

    def test_extract_json(self):
        """test extract_json"""
        DataTuple = namedtuple('DataTuple',
                               ['type_status', 'token', 'messages'])

        json_msg = {"response": {"type": "ok",
                                 "message": "Direct message sent"}}
        msg_np1 = DataTuple(type_status=json_msg["response"]["type"], token='',
                            messages=json_msg["response"]["message"])
        json_msg = json.dumps(json_msg)
        assert msg_np1 == extract_json(json_msg)

        json_msg = {"response": {"type": "ok", "messages": 'Welcome!',
                                 "token":
                                     '6e79a5fd-2b96-4c48-8ae5-938c8dbb0e54'}}
        msg_np2 = DataTuple(type_status=json_msg["response"]["type"],
                            token=json_msg["response"]["token"],
                            messages=json_msg["response"]["messages"])
        json_msg = json.dumps(json_msg)
        result_np2 = extract_json(json_msg)
        assert msg_np2 == result_np2

        json_msg = '{"response": {"type": "ok", ' \
                   '"message": "Direct message sent",}'
        msg_np2 = None
        assert msg_np2 == extract_json(json_msg)

    def test_directmessage(self):
        """test DirectMessage()"""
        directmessage = DirectMessage()
        recipient = 'nicaiwoshishei'
        message = 'nihao'
        time = '20230321'
        directmessage.recipient = recipient
        directmessage.message = message
        directmessage.timestamp = time
        assert directmessage.recipient == 'nicaiwoshishei'
        assert directmessage.message == 'nihao'
        assert directmessage.timestamp == '20230321'

    def test_send(self):
        """test send()"""
        ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                                       username="VC1",
                                       password="VC")
        result = ds_messenger.send(message="this is juan",
                                   recipient="nicaiwoshishei")
        assert result

        ds_messenger = DirectMessenger(dsuserver="168.235.86.102",
                                       username="VC1",
                                       password="VC")
        result = ds_messenger.send(message="this is juan",
                                   recipient="nicaiwoshishei")
        assert not result

    def test_retrieve_new(self):
        """test retrieve_new()"""
        ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                                       username="nicaiwoshishei",
                                       password="buxiangshuohua")
        objs = ds_messenger.retrieve_new()
        assert isinstance(objs, list)

    def test_retrieve_all(self):
        """test retrieve_all()"""
        ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                                       username="nicaiwoshishei",
                                       password="buxiangshuohua")
        ds_messenger.connect()
        objs = ds_messenger.retrieve_all()
        assert isinstance(objs, list)


if __name__ == "__main__":
    unittest.main()
