import os

import json
import getpass

file_path = os.path.abspath('.')
file_name = 'users.json'
def load_users():
    '''
    load users json
    '''
    users = None
    try:
        with open(f'{file_path}/{file_name}', 'r') as temp_file:
            users = json.load(temp_file)
        return users
    except FileNotFoundError as exc:
        pass


users = load_users()

uname = input('username: ')
passw = getpass.getpass('passw: ')

loged_user = None

for index in users:
    if uname in index['name'] and passw in index['passw']:
        loged_user = index

if loged_user:
    print(f"Logged in as {loged_user['name']}")
else:
    print('user not found!')
