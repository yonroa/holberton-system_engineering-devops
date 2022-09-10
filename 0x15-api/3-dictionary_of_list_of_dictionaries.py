#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her TODO list progress
"""
import requests
import json
if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    user_dict = {}
    user_name_dict = {}
    for user in users:
        uid = user.get('id')
        user_dict[uid] = []
        user_name_dict[uid] = user.get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for task in todo:
        taskdict = {}
        uid = task.get('userId')
        taskdict['task'] = task.get('title')
        taskdict['completed'] = task.get('completed')
        taskdict['username'] = user_name_dict.get(uid)
        user_dict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as file:
        json.dump(user_dict, file)
