#!/usr/bin/python3
"""Using this REST API, function accept an integer as paramete
Return: display on the standard output the employee TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    id_employee = sys.argv[1]
    general = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           id_employee)
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         id_employee + '/todos')
    name_employee = general.json()['name']
    tasks_employee = tasks.json()
    completed = []
    for task in tasks_employee:
        if task['completed'] is True:
            completed.append(task)
    print('Employee {} is done with tasks ({}/{}):'
          .format(name_employee, len(completed), len(tasks_employee)))
    for title in completed:
        print("\t" + title['title'], end="\n")
