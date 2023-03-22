"""
The main code for running the whole program
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
# username = "nicaiwoshishei", password = "buxiangshuohua"
# token='6e79a5fd-2b96-4c48-8ae5-938c8dbb0e54'
# username = "IM10", password = "im10",
# token='f5ad9862-29b1-4b6e-b654-5a45133149b6'

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
                    else:
                        print("\nINVALID OPTION! Please enter a valid option.")

                    ep_inputs = start(prompt=2)
        else:
            print("\nINVALID OPTION! Please enter a valid option.")

        inputs = start(prompt=0)


if __name__ == "__main__":
    user()
