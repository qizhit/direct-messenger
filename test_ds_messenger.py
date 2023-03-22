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

    def test_extract_json(self):
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


if __name__ == "__main__":
    unittest.main()
