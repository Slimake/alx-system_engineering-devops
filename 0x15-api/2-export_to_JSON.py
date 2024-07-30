#!/usr/bin/python3
"""
Using what you did in the task #0

Extend your Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":

    _id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/' + _id)

    todos = requests \
        .get('https://jsonplaceholder.typicode.com/todos?userId=' + _id)

    user = user.json()
    todos = todos.json()

    USER_ID = user.get('id')
    TASKS = []
    filename = f'{USER_ID}.json'

    # Loop through todos
    for todo in todos:
        TASKS.append({
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': user.get('username')
                })

    dic = {USER_ID: TASKS}

    # Open and save into file
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(dic, jsonfile)
