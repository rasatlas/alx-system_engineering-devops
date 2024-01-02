#!/usr/bin/python3
"""
Python script that, using https://jsonplaceholder.typicode.com/ REST API,
gather data and export it as a JSON dictionary file.
"""
import re
import requests
import sys


base_url = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(base_url)).json()
    todos_res = requests.get('{}/todos'.format(base_url)).json()
    users_data = {}
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
