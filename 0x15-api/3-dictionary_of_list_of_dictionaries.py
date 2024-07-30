#!/usr/bin/python3
"""
Using what you did in the task #0

Extend your Python script to export data in the JSON format
"""
import json
import requests

if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users')

    todos = requests \
        .get('https://jsonplaceholder.typicode.com/todos')

    users = users.json()
    todos = todos.json()

    all_users = {}
    filename = 'todo_all_employees.json'

    for user in users:
        USER_ID = user.get('id')
        TASKS = []

        # Loop through todos
        for todo in todos:
            if USER_ID == todo.get('userId'):
                TASKS.append({
                        'username': user.get('username'),
                        'task': todo.get('title'),
                        'completed': todo.get('completed')
                    })

        all_users.update({USER_ID: TASKS})

    # Open and save into file
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(all_users, jsonfile)
