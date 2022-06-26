import os
import getpass

if not os.path.exists('records.txt'):
    open('records.txt', 'w').close()
    exit()


def register():
    print('=====New User Recording=====')
    username = input('Enter your username:')
    n = username.lstrip()
    u = n.rstrip()
    if username in open('records.txt', 'r').read():
        print('Record already exists')
        exit()
    password = getpass.getpass('Enter your password:')
    p = password.lstrip()
    pp = p.rstrip()
    conform_password = getpass.getpass('Conform your password:')
    cp = conform_password.lstrip()
    cpp = conform_password.rstrip()
    if pp != cpp:
        print('Password does not match!')
        exit()
    with open('records.txt', 'a') as f:
        f.write(f"Username:{u},Password:{pp}")
        f.write('\n')
        print('Successfully registered')
        exit()


# register()


def login():
    uname = input('Enter your username:')
    n = uname.lstrip()
    u = n.rstrip()
    if uname in open('records.txt','r').read():
        password = getpass.getpass('Enter your password:')
        p = password.lstrip()
        pp = p.rstrip()
        data = open('records.txt', 'r')
        users = data.readlines()
        for a in users:
            b = a.split()
            print(b[0][::-3])
    else:
        print('You have not been registered,Please register first.')
login()