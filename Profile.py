# Profile.py
#
# ICS 32
# Assignment #2: Journal
#
# Author: Mark S. Baldwin, modified by Alberto Krone-Martins
#
# v0.1.9

# You should review this code to identify what features you need to support
# in your program for assignment 2.
#
# YOU DO NOT NEED TO READ OR UNDERSTAND THE
# JSON SERIALIZATION ASPECTS OF THIS CODE
# RIGHT NOW, though can you certainly
# take a look at it if you are curious since we
# already covered a bit of the JSON format in class.
#
# Qizhi Tian
# qizhit@uci.edu
# 45765950

import json
import time
from pathlib import Path


"""
DsuFileError is a custom exception handler that you should
catch in your own code. It is raised when attempting to
load or save Profile objects to file the system.

"""


class DsuFileError(Exception):
    pass


"""
DsuProfileError is a custom exception handler that you should
catch in your own code. It is raised when attempting to
deserialize a dsu file to a Profile object.

"""


class DsuProfileError(Exception):
    pass


class Profile:
    """
    The Profile class exposes the properties required to
    join an ICS 32 DSU server. You
    will need to use this class to manage the information
    provided by each new user
    created within your program for a2. Pay close attention
    to the properties and
    functions in this class as you will need to make use of
    each of them in your program.

    When creating your program you will need to collect user
    input for the properties
    exposed by this class. A Profile class should ensure that
    a username and password
    are set, but contains no conventions to do so. You should
    make sure that your code
    verifies that required properties are set.

    """

    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver  # REQUIRED
        self.username = username  # REQUIRED
        self.password = password  # REQUIRED
        self.retrieve = {}

    """

    add_post accepts a Post object as parameter and appends it
    to the posts list. Posts are stored in a list object
    in the order they are added. So if multiple Posts objects are created,
    but added to the Profile in a different order, it is possible for the
    list to not be sorted by the Post.timestamp property.
    So take caution as to how you implement your add_post code.

    """
    def init_retrieve(self, direct_obj):
        self.retrieve = {}
        for obj in direct_obj:
            if obj.recipient not in self.retrieve.keys():
                self.retrieve[obj.recipient] = []
            self.retrieve[obj.recipient].append(obj.message)

    def add_friend(self, direct_obj):
        for obj in direct_obj:
            if obj.recipient not in self.retrieve.keys():
                self.retrieve[obj.recipient] = []
            self.retrieve[obj.recipient].append(obj.message)

    """

    save_profile accepts an existing dsu file to
    save the current instance of Profile to the file system.

    Example usage:

    profile = Profile()
    profile.save_profile('/path/to/file.dsu')

    Raises DsuFileError

    """
    def save_profile(self, path: str) -> None:
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'w')
                json.dump(self.__dict__, f)
                f.close()
            except Exception as ex:
                raise DsuFileError("Error while attempting "
                                   "to process the DSU file.", ex)
        else:
            raise DsuFileError("Invalid DSU file path or type")

    """

    load_profile will populate the current instance of Profile
    with data stored in a DSU file.

    Example usage:

    profile = Profile()
    profile.load_profile('/path/to/file.dsu')

    Raises DsuProfileError, DsuFileError

    """
    def load_profile(self, path: str) -> None:
        p = Path(path)

        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                # self.retrieve = obj['retrieve']
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()
