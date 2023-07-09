#!/usr/bin/python3
"""Script that returns employee's to-do list"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todo" \
        .format(employee_id)
  
    user_info = requests.get(user_url).json()
    todo_info = requests.get(todo_url).json()

    employee_name = user_info["name"]
    completed_tasks = list(filter(lambda task:
                                  (task["completed"] is True), todo_info))
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, num_completed_tasks, total_tasks))

    [print("\t " + task["title"]) for task in completed_tasks]
