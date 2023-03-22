"""
The user interface code
"""

# ui.py

# Qizhi Tian
# qizhit@uci.edu
# 45765950

import sys

# Starter code for assignment 2 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950

from command import *
from Profile import *
from ds_messenger import *


def start(prompt):
    """the greeting and prompt when start"""
    if prompt == 0:
        print("\nWhat would you like to do: \n"
              "c: create a dsu file and loat it at the same time\n"
              "   (You can add the profile/posts or "
              "upload them online after creating the file.)\n"
              "o: load a existing dsu file\n"
              "   (You can edit the profile/posts or "
              "upload them online after loading the file.)\n"
              "l: list the content of a directory\n"
              "r: read a dsu file\n"
              "d: delete a dsu file\n"
              "q: exit the program\n")
    elif prompt == 1:
        print("You can edit or print your profile and posts!\n"
              "   e - edit your profile or posts\n"
              "   p - print your profile or posts\n"
              "If you don't want to continue to "
              "edit, print, or upload your profile and posts, "
              "you can enter 'back' or 'q'.\n"
              "   enter 'back' to return\n"
              "   enter 'q' to exit the program\n")
    elif prompt == 2:
        print("\nDo you want to continue to edit or print "
              "your profile and posts?\n"
              "   enter 'e' to edit\n"
              "   enter 'p' to print\n"
              "If you don't want to continue to you can enter 'back' or 'q'.\n"
              "   enter 'back' to return\n"
              "   enter 'q' to exit the program\n")
    inputs = input().strip()
    return inputs


def user_r():
    """UI function to read a dsu file"""
    path = input("please enter your file(.dsu) path: \n").strip()
    path = Path(path)
    try:
        print("\nHere's your content of the file.\n")
        read(path)
    except (IsADirectoryError, FileNotFoundError):
        print("ERROR! Please make sure your file exists and has "
              "a '.dsu' suffix")


def user_d():
    """UI function to delete a dsu file for UI"""
    path = input("please enter the path of your file(.dsu) "
                 "that you want to delete: \n").strip()
    path = Path(path)
    d_input = f"D {path}"
    result = delete(d_input, path)
    if result:
        print("\nYour file is deleted successfully!")


def user_l():
    """UI function to list the content"""
    print("\nYour have several options: \n"
          "   ls - only list the content of the current directory\n"
          "   rls - recursively list the content of the directory\n"
          "   f - only list the file of the current directory\n"
          "   rf - recursively list the file of the current directory\n"
          "   s - only list the specified file of the current directory\n"
          "   rs - recursively list the specified file of the directory\n"
          "   e - only list the file with specified suffix "
          "of the current directory\n"
          "   re - recursively list the file with "
          "specified suffix of the directory\n"
          "If you don't want to continue, you can enter 'back' or 'q'.\n"
          "   enter 'back' to return\n"
          "   enter 'q' to exit the program\n")
    opt = input().strip()
    option, path, filename, suffix = '', '', '', ''

    if opt in ['ls', 'rls', 'f', 'rf', 's', 'rs', 'e', 're']:
        path = input("Please enter your directory path: \n")
        path = Path(path)
        if opt in ['ls', 'rls', 'f', 'rf']:
            if opt == 'ls':
                option = ''
            elif opt == 'rls':
                option = '-r'
            elif opt == 'f':
                option = '-f'
            elif opt == 'rf':
                option = '-r -f'
        elif opt in ['s', 'rs']:
            if opt == 's':
                option = '-s'
            elif opt == 'rs':
                option = '-r -s'
            filename = input("Please enter your file name (e.g file.txt): \n")
        elif opt in ['e', 're']:
            if opt == 'e':
                option = '-e'
            elif opt == 're':
                option = '-r -e'
            suffix = input("Please enter your file suffix (e.g. 'txt'): \n")
            suffix = '.' + suffix
        try:
            print()
            result = iterate(path, option, filename, suffix)
            if not result:  # result == False
                user_l()
        except FileNotFoundError:
            print('NO SUCH FILE/DIRECTORY')
            user_l()
    elif opt == 'back':
        return
    elif opt in ('q', 'Q'):
        sys.exit()
    else:
        print("\nINVALID OPTION! Please enter a valid option.")
        user_l()


def user_c():
    """UI function to create a dsu file and load it at the same time"""
    # get username, password, and bio; edit to profile
    dsuserver = input("Please enter the server location (IP address): \n")

    username = input("Please enter your username: \n")
    while username == '' or username.isspace():
        username = input("Sorry, username cannot be empty or whitespaces.\n"
                         "Please enter your username: \n")
    password = input("Please enter your password: \n")
    while password == '' or password.isspace():
        password = input("Sorry, password cannot be empty or whitespaces.\n"
                         "Please enter your password: \n")

    profile = Profile(dsuserver=dsuserver, username=username,
                      password=password)

    bio_answer = input("Do you want to set your bio? (y/n): ")
    if bio_answer in ['y', 'Y']:
        bio = input("Please enter your bio: \n")
        while bio == '' or bio.isspace():
            bio = input("Sorry, bio cannot be empty or whitespaces.\n"
                        "Please enter your bio: \n")
        profile.bio = bio

    # get the path and create the file
    path = input("Please enter the directory where you want to "
                 "save the dsu file: \n").strip()
    create_name = input("Please enter the file name without its suffix: \n")
    path = Path(path)
    new_path = path / create_name

    if new_path.exists():
        print("\nYour file is already exist!")
    else:
        try:
            path = create(path, create_name)
            save(profile, path)
            path = str(path)
            print("\nYour file is created successfully! "
                  "Here's your file path: \n\n" + path)
        except FileNotFoundError:
            print("\nNO SUCH FILE/DIRECTORY", end='')

    return profile, path


def user_e(profile, path):
    """UI function to edit the profile and posts"""
    print("\nYou have several options: \n"
          "   usr - edit the username for your profile\n"
          "   pwd - edit the password for your profile\n"
          "   bio - edit the bio "
          "(a brief description of you) for your profile\n"
          "   add - add a post to your dsu file\n"
          "   del - del a post to your dsu file\n")
    option = input().strip()

    inputs = ''
    if option in ['usr', 'pwd', 'bio']:
        info = ''
        if option == 'usr':
            info = 'username'
        elif option == 'pwd':
            info = 'password'
        elif option == 'bio':
            info = 'bio'
        if info != '':
            info_input = input(f"Please enter the {info}: \n")
            while info_input == '' or info_input.isspace():
                info_input = input(f"Sorry, {info} cannot be empty or "
                                   f"whitespaces.\n"
                                   f"Please enter the {info}: \n")
            inputs = f"E -{option} \"{info_input}\""
    elif option == 'add':
        post = input("There are two keywords you can choose: \n"
                     "@weather: the description of the weather\n"
                     "@lastfm: the hottest music tag name\n\n"
                     "Please enter the post that you want to add: \n")
        while post == '' or post.isspace():
            post = input(f"Sorry, the post cannot be empty or whitespaces.\n"
                         f"Please enter the post: \n")
        inputs = f"E -{option}post \"{post}\""
    elif option == 'del':
        print("Here's your posts.\n")
        posts = profile.get_posts()
        for i, post in enumerate(posts):
            print(f"{i + 1}. {post}")
        post_id = input("\nPlease enter the NUMBER of the post "
                        "that you want to delete: \n")
        inputs = f"E -{option}post {post_id}"
    else:
        print("\nINVALID OPTION! Please enter a valid option.")
        return

    e_command(profile, path, inputs)
    print("\nYour profile is edited successfully!")


def user_p(profile, path):
    """UI function to print the profile and posts"""
    print("\nYou have several options: \n"
          "   usr - print the username of your profile\n"
          "   pwd - print the password of your profile\n"
          "   bio - print the bio of your profile\n"
          "   posts - print all posts of your file\n"
          "   post - print a certain post of your file\n"
          "   all - print all information of your file\n")
    option = input().strip()

    posts_len = len(profile.get_posts())
    if option in ['post', 'posts'] and posts_len == 0:
        print("\nSorry, you don't have any post now.")
        return
    if option in ['usr', 'pwd', 'bio', 'posts', 'all']:
        inputs = f"P -{option}"
    elif option == 'post':
        print(f"\nNow you have {posts_len} post/posts.")
        post_id = input("Please enter the NUMBER of the post "
                        "that you want to print: \n")
        inputs = f"P -{option} {post_id}"
    else:
        print("\nINVALID OPTION! Please enter a valid option.")
        return

    print("Here's your information: \n")
    p_command(profile, path, inputs)
