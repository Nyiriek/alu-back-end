#!/usr/bin/python3
"""Script that returns employee's to-do list"""

import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/users/1/todos/"
    user = requests.get(user_url, query_params={"Id": employeeId})
    todo = requests.get(todo_url, query_params={"employeeId": employeeId})
    
    user_data = user.json()
    todo_data = todo.json() 
    
    completed_tasks = []
    total_tasks = len(todo_data)
    employee = user_data[0].get("name")

    for task in todo_data:
        if task["completed"]:
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(completed_tasks), total_tasks))
    
    for task in completed_tasks:
        print("\t ".format(task.get("title")))
