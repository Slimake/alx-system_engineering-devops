#!/usr/bin/python3
"""
Using what you did in the task #0

Extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)

    todos = requests \
        .get('https://jsonplaceholder.typicode.com/todos?userId=' + id)

    user = user.json()
    todos = todos.json()

    USER_ID = user.get('id')
    USERNAME = user.get('username')
    TASK_COMPLETED_STATUS = []
    TASK_TITLE = []
    filename = f'{USER_ID}.csv'

    for todo in todos:
        TASK_COMPLETED_STATUS.append(todo.get('completed'))
        TASK_TITLE.append(todo.get('title'))

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv \
          .writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for STATUS, TITLE in zip(TASK_COMPLETED_STATUS, TASK_TITLE):
            csv_writer.writerow([USER_ID, USERNAME, STATUS, TITLE])
