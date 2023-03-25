"""
test profile.py
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

import unittest
from pathlib import Path
from ds_messenger import DirectMessenger
from Profile import Profile


class TestProfile(unittest.TestCase):
    """test profile"""

    def test_init_retrieve(self):
        """test_init_retrieve"""
        ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                                       username="nicaiwoshishei",
                                       password="buxiangshuohua")
        objs = ds_messenger.retrieve_all()
        profile = Profile(dsuserver="168.235.86.101",
                          username="nicaiwoshishei",
                          password="buxiangshuohua")
        profile.init_retrieve(objs)
        assert isinstance(objs, list)

    def test_add_friend(self):
        """test_add_friend"""
        ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                                       username="nicaiwoshishei",
                                       password="buxiangshuohua")
        objs = ds_messenger.retrieve_all()
        profile = Profile(dsuserver="168.235.86.101",
                          username="nicaiwoshishei",
                          password="buxiangshuohua")
        profile.add_friend(objs)
        assert isinstance(objs, list)

    def test_load_save_profile(self):
        """test_save_profile"""
        profile = Profile()
        root = '.'
        filename = 'test.dsu'
        path = Path(root) / Path(filename)
        profile.load_profile(str(path))
        profile.save_profile(str(path))
        assert profile.username == '101010'


if __name__ == "__main__":
    unittest.main()
