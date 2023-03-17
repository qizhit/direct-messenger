"""
code to connect service using socket
"""

# Starter code for assignment 3 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950
import socket
import time
from ds_protocol import *


def post_online(message, send_2, token, timestamp, recv1):
    """send the post online"""
    online_post = server_post(token, message, timestamp)  # get the post
    send_2.write(online_post + '\r\n')
    send_2.flush()
    resp1 = recv1.readline()
    # if type == 'error'，return False
    resp1_np = extract_json(resp1)

    if resp1_np.type_status == 'error':
        return False

    print("\nYour post is uploaded successfully!")
    return True


def bio_online(bio, send_2, token, timestamp, recv1):
    """send the bio online"""
    online_bio = server_bio(token, bio, timestamp)  # get the bio
    send_2.write(online_bio + '\r\n')
    send_2.flush()
    resp2 = recv1.readline()
    # if type == 'error'，return False
    resp2_np = extract_json(resp2)

    if resp2_np.type_status == 'error':
        return False

    print("Your bio is uploaded successfully!")
    return True


def post_entry(post_dict):
    """collect the post that need to upload online"""
    u_post = post_dict["entry"]
    return u_post


def send(server: str, port: int, username: str, password: str, message: str,
         bio: str = None):
    """
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port))

            join_msg = msg_join(username, password)

            send_1 = client.makefile('w')
            recv = client.makefile('r')
            send_1.write(join_msg + '\r\n')
            send_1.flush()
            resp = recv.readline()
            resp_np = extract_json(resp)
            print(resp_np)

            if resp_np.type_status != 'ok':
                return False

            token = resp_np.token
            timestamp = time.time()

            send_2 = client.makefile('w')
            recv1 = client.makefile('r')

            if (message is not None) and \
                    (message != '') and not message.isspace():
                result = \
                    post_online(message, send_2, token, timestamp, recv1)
                if not result:
                    return False

            if (bio is not None) and (bio != '') and not bio.isspace():
                result = bio_online(bio, send_2, token, timestamp, recv1)
                if not result:
                    return False

            return True

    except (ConnectionRefusedError, socket.gaierror, TypeError, NameError):
        return False
