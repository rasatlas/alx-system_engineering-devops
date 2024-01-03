#!/usr/bin/python3
"""
Python script that, using https://jsonplaceholder.typicode.com/ REST API,
gathers data and exports it to JSON file.
"""
import json
import re
import requests
import sys


base_url = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(base_url, id)).json()
            todos_res = requests.get('{}/todos'.format(base_url)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open("{}.json".format(id), 'w') as json_file:
                user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_name
                    },
                    todos
                ))
                user_data = {
                    "{}".format(id): user_data
                }
                json.dump(user_data, json_file)
