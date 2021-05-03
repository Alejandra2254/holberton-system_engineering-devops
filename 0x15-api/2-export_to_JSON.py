#!/usr/bin/python3
"""Using this REST API, function accept an integer as paramete
Return: extend your Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    id_employee = sys.argv[1]
    general = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           id_employee)
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         id_employee + '/todos')
    user_employee = general.json()['username']
    tasks_employee = tasks.json()
    name_file = id_employee + '.json'
    with open(name_file, 'w', newline='') as f:
        list = []
        for task in tasks_employee:
            task_dict = {}
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            task_dict["username"] = user_employee
            list.append(task_dict)
        dict_final = {}
        dict_final[id_employee] = list
        json.dump(dict_final, f)
