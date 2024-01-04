#!/usr/bin/python3
"""
A Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_USERNAME = user.get('username')
            break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    with open('2.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos.json():
            if todo.get('userId') == int(argv[1]):
                writer.writerow([
                    todo.get('userId'), EMPLOYEE_USERNAME,
                    todo.get('completed'), todo.get('title')])
