#!/usr/bin/python3
"""Using this REST API, function accept an integer as paramete
Return: extend your Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    request_1 = requests.get('https://jsonplaceholder.typicode.com/users/')
    general = request_1.json()
    dict_final = {}
    for user in general:
        id_employee = str(user['id'])
        r_2 = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           id_employee)
        r_3 = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           id_employee + '/todos/')
        user_employee = r.json()['username']
        tasks_employee = r_3.json()
        list = []
        for task in tasks_employee:
            task_dict = {}
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            task_dict["username"] = user_employee
            list.append(task_dict)
            dict_final[id_employee] = list
    json_txt = json.dumps(dict_final)
    with open("todo_all_employees.json", 'w') as f:
        f.write(json_txt)
