#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her TODO list progress
"""
import requests
import sys
if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
