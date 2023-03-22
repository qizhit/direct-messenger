"""
a5.py
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

# 168.235.86.101

from ds_messenger import DirectMessenger
from Profile import Profile


def store_msg(dsuserver, username, password):
    ds_messenger = DirectMessenger(dsuserver=dsuserver,
                                   username=username,
                                   password=password)
    ds_messenger.connect()
    new_obj = ds_messenger.retrieve_new()
    all_obj = ds_messenger.retrieve_all()
    new_msg = []
    all_msg = []
    for msg in new_obj:
        new_msg.append(msg.message)
    for msg in all_obj:
        all_msg.append(msg.message)

    profile = Profile(dsuserver=dsuserver, username=username,
                      password=password)
    profile.new = new_msg
    profile.all = all_msg


if __name__ == "__main__":
    store_msg("168.235.86.101", "nicaiwoshishei", "buxiangshuohua")
