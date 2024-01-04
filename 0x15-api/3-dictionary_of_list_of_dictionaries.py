#!/usr/bin/python3
"""
A Python script to export data in the JSON format for all employees.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    # Make an API call to users endpoint
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    # Loop through all users
    USERS = []
    for user in users.json():
        USERS.append((user.get('id'), user.get('username')))

    # Make an API call to todos endpoint
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    # Loop through todos until argv[1] matches todo UserId
    TASKS = []
    for todo in todos.json():
        TASKS.append((
            todo.get('userId'),
            todo.get('title'),
            todo.get('completed')))

    # Export to JSON
    data = dict()
    for user in USERS:
        USER_TASKS = []
        for task in TASKS:
            if (user[0] == task[0]):
                USER_TASKS.append({
                    "username": user[1],
                    "task": task[1],
                    "completed": task[2]})
        data[str(user[0])] = USER_TASKS

    filename = "todo_all_employees.json"
    with open(filename, 'w') as JSON_file:
        json.dump(data, JSON_file)
