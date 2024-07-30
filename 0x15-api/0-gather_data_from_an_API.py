#!/usr/bin/python3
"""
A python script that uses a REST API for a given employee ID

Returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users?id=' + id)

    todos = requests \
        .get('https://jsonplaceholder.typicode.com/todos?userId=' + id)

    user = user.json()
    todos = todos.json()
    done_tasks = 0
    total_number_of_tasks = len(todos)
    TASK_TITLE = []

    for todo in todos:
        if todo.get('completed') is True:
            done_tasks += 1
            TASK_TITLE.append(todo.get('title'))

    if len(user) > 0 and user[0].get('id') == int(id):
        print(f"Employee {user[0].get('name')} is done with "
              f"tasks({done_tasks}/{total_number_of_tasks}):")

    for title in TASK_TITLE:
        print(f"\t {title}")
