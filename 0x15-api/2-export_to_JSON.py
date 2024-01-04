#!/usr/bin/python3
"""
A Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_USERNAME = user.get('username')
            break
    USER_TASKS = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            USER_TASKS.append({"task": todo.get('title'), "completed": todo.get('completed'), "username": EMPLOYEE_USERNAME})
    
    filename = "{}.json".format(argv[1])
    with open(filename, 'w') as JSON_file:
        json.dump({argv[1]: USER_TASKS}, JSON_file)
#{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},