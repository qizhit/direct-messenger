"""
The command code
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

from pathlib import Path
from Profile import DsuFileError, DsuProfileError, Post
from OpenWeather import OpenWeather
from LastFM import LastFM

CHECK = False


def iterate_r_f(path, option):
    """process the '-r', '-f', and '-r -f' options"""
    my_dir = []
    for i in path.iterdir():
        if i.is_file():
            print(i)
        elif i.is_dir():
            my_dir.append(i)

    if option == '':
        for i in my_dir:
            print(i)
    elif option == '-r':
        for i in my_dir:
            print(i)
            iterate_r_f(i, option)
    elif option == '-f':
        pass
    elif option == '-r -f':
        for i in my_dir:
            iterate_r_f(i, option)


def iterate_s_rs(path, option, filename):
    """process '-s' and '-r -s' optioins"""
    global CHECK
    if filename != '':
        for i in path.iterdir():
            if i.name == filename:
                print(i)
                CHECK = True
            elif option == '-r -s' and i.is_dir():
                iterate_s_rs(i, option, filename)


def iterate_e_re(path, option, suffix):
    """process '-e' and '-r -e' optioins"""
    global CHECK
    if suffix != '':
        for i in path.iterdir():
            if i.suffix == suffix:
                print(i)
                CHECK = True
            elif option == '-r -e' and i.is_dir():
                iterate_e_re(i, option, suffix)


def iterate(path, option, filename, suffix):
    """process L command and call its option functions"""
    if option == '':
        iterate_r_f(path, option)
    elif option in ['-r', '-f', '-r -f']:
        iterate_r_f(path, option)
    elif option in ['-s', '-r -s']:
        iterate_s_rs(path, option, filename)
        # if no file named [filename], CHECK == False
        if (not CHECK) or (filename == ''):
            print('NO SUCH FILE/DIRECTORY')
            return False
    elif option in ['-e', '-r -e']:
        iterate_e_re(path, option, suffix)
        if (not CHECK) or suffix == '.':
            print('NO SUCH FILE/DIRECTORY')
            return False
    return True


def create(path, create_name):
    """process C command, creating a new dsu file and load it"""
    new_name = create_name + '.dsu'
    new_path = path / Path(new_name)
    if not new_path.exists():
        new_path.touch(exist_ok=True)
    return new_path


def delete(inputs, path):
    """process the D command, deleting a dsu file"""
    if (not path.exists()) or (inputs[-4:] != '.dsu'):
        print("ERROR! Please make sure your file exists and has "
              "a '.dsu' suffix")
        return False

    path.unlink(missing_ok=False)
    return True


def read(path):
    """process R command, reading a dsu file"""
    with path.open() as file:
        if path.suffix == '.dsu':
            if path.stat().st_size != 0:
                for i in file:
                    print(i.strip('\n'))
            else:
                print('EMPTY')
        else:
            print('ERROR')


def load(profile, path):
    """call load_profile function and process its exception"""
    try:
        profile.load_profile(path)
        return True
    except DsuProfileError:
        print('\nError while attempting to load the file.')
        return 'Error while attempting to load the file.'
    except DsuFileError:
        print('\nError while attempting to load the file.')
        return 'Error while attempting to load the file.'


def save(profile, path):
    """call the save_profile function and process its exception"""
    try:
        profile.save_profile(path)
    except DsuFileError as e:
        print(e)


def api_call(addpost):
    """
    call the class MYAPI (OpenWeather and LastFM)
    """
    if "@weather" in addpost:
        zipcode = input("\nPlease enter zip code: ")
        ccode = input("Please enter country code: ")
        weather_apikey = input("Please enter your OpenWeather api key "
                               "(You can also use my api key "
                               "7cc3de7bc963865a05395ff953aa1bcf): ")
        openweather = OpenWeather(zip_code=zipcode, c_code=ccode)
        openweather.set_apikey(weather_apikey)
        openweather.load_data()
        addpost = openweather.transclude(message=addpost)

    if "@lastfm" in addpost:
        lastfm_apikey = input("\nPlease enter your LastFM api key "
                              "(You can also use my api key "
                              "29f34099931d760c0a78dbfdd6d4ef9f): ")
        lastfm = LastFM()
        lastfm.set_apikey(lastfm_apikey)
        lastfm.load_data()
        addpost = lastfm.transclude(message=addpost)

    return addpost


def e_option(inputs):
    """process the options of E/edit command"""
    e_option_dict = {'-usr': None, '-pwd': None, '-bio': '', '-addpost': '',
                     '-delpost': ''}
    mylist = inputs.split('-')

    for key in e_option_dict:
        for ele in mylist:
            ele = '-' + ele
            if key in ele:
                value = ele.strip(key).strip().strip('"').strip("'")
                e_option_dict[key] = value
    username = e_option_dict['-usr']
    password = e_option_dict['-pwd']
    bio = e_option_dict['-bio']
    addpost = e_option_dict['-addpost']
    if ("@weather" in addpost) or ("@lastfm" in addpost):
        addpost = api_call(addpost)

    del_id = e_option_dict['-delpost']

    return username, password, bio, addpost, del_id


def e_command(profile, path, inputs):
    """process the E/edit command"""
    username, password, bio, addpost, del_id = e_option(inputs)
    if username is not None:
        profile.username = username
    if password is not None:
        profile.password = password
    if bio != '':
        profile.bio = bio
    if addpost != '':
        post = Post(entry=addpost)
        profile.add_post(post)
    if del_id != '':
        try:
            del_id = int(del_id)
            profile.del_post(del_id - 1)
        except ValueError:
            print('ERROR')
    save(profile, path)


def p_option(inputs):
    """process the options of P/print command"""
    mylist = inputs.split()
    p_options = []
    post_id = ''
    for opt in mylist:
        if opt.startswith('-'):
            p_options.append(opt)
            try:
                if opt == '-post':
                    index = mylist.index(opt)
                    post_id = mylist[index + 1]
                    post_id = int(post_id)
            except ValueError:
                print('ERROR')

    return p_options, post_id


def p_command(profile, path, inputs):
    """process the P/print command"""
    p_options, post_id = p_option(inputs)
    for opt in p_options:
        if opt == '-usr':
            print(profile.username)
        elif opt == '-pwd':
            print(profile.password)
        elif opt == '-bio':
            print(profile.bio)
        elif opt == '-posts':
            posts = profile.get_posts()
            for i, post in enumerate(posts):
                print(f"{i + 1}. {post}")
        elif opt == '-post':
            try:
                posts = profile.get_posts()
                print(posts[post_id - 1])
            except TypeError:
                pass
            except IndexError:
                print('ERROR')
        elif opt == '-all':
            with open(path, 'r') as file:
                print(file.read())
