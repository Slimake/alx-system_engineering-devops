#!/usr/bin/python3
"""
A Python script, using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    EMPLOYEE_NAME = ''
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = user.get('name')
        break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))
            TOTAL_NUMBER_OF_TASKS += 1
    print('Employee {} is done with tasks({}/{})'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print('\t {}'.format(title))
