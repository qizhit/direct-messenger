"""
The main code
"""

# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950

# server = '168.235.86.101'
# port = 3021

from ui import *


def user():
    """the user interface outline"""
    print("\nWelcome!")
    inputs = start(prompt=0)

    while inputs not in ('q', 'Q'):
        if inputs in ('r', 'R'):
            user_r()

        elif inputs in ('d', 'D'):
            user_d()

        elif inputs in ('l', 'L'):
            user_l()

        elif (inputs in ('o', 'O')) or \
                inputs in ('c', 'C'):
            profile = Profile()
            path = ''

            if inputs in ('o', 'O'):
                path = input("Please enter your file(.dsu) path: \n").strip()
            elif inputs in ('c', 'C'):
                profile, path = user_c()

            load_resp = load(profile, path)
            if load_resp is True:
                print("\nYour file is loaded successfully!\n")

                ep_inputs = start(prompt=1)
                while True:
                    if ep_inputs == 'back':
                        break
                    if ep_inputs in ('q', 'Q'):
                        sys.exit()
                    elif ep_inputs in ('e', 'E'):
                        user_e(profile, path)

                    elif ep_inputs in ('p', 'P'):
                        user_p(profile, path)

                    elif ep_inputs in ('u', 'U'):
                        try:
                            user_u(profile)
                        except UnboundLocalError:
                            print('Error. No server location/IP address')
                    else:
                        print("\nINVALID OPTION! Please enter a valid option.")

                    ep_inputs = start(prompt=2)
        else:
            print("\nINVALID OPTION! Please enter a valid option.")

        inputs = start(prompt=0)


if __name__ == "__main__":
    user()
