#!/usr/bin/python3
"""A script that exports data in csv format"""

import csv
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    url_todo = f'https://jsonplaceholder.typicode.com/users/{employeeId}/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    todo = requests.get(url_todo, params={'userId': employeeId})
    user = requests.get(url_user, params={'id': employeeId})

    todo_data = todo.json()
    user_data = user.json()

    completed_tasks = []
    employee_name = user_data[0].get('name')

    for task in todo_data:
        if task['completed']:
            completed_tasks.append(task)

    csv_file_name = f'{employeeId}.csv'

    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in completed_tasks:
            writer.writerow([employeeId, employee_name, "Completed", task.get('title')])

    print(f"Data exported to {csv_file_name} successfully.")
