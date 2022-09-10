#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her TODO list progress
"""
import sys
import requests
import json
if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()
    tasks = []
    for data in todo:
        task_dic = {}
        task_dic['task'] = data.get('title')
        task_dic['completed'] = data.get('completed')
        task_dic['username'] = user.get('username')
        tasks.append(task_dic)
    objson = {}
    objson[sys.argv[1]] = tasks
    with open("{}.json".format(sys.argv[1]), 'w') as file:
        json.dump(objson, file)
