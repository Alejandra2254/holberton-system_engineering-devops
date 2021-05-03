#!/usr/bin/python3
"""Using this REST API, function accept an integer as paramete
Return: display on the standard output the employee TODO list progress"""
import requests
import sys
import csv


if __name__ == "__main__":
    id_employee = sys.argv[1]
    general = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           id_employee)
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         id_employee + '/todos')
    user_employee = general.json()['username']
    tasks_employee = tasks.json()
    name_file = id_employee + '.csv'
    with open(name_file, 'w', newline='') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks_employee:
            list = []
            list.append(id_employee)
            list.append(user_employee)
            list.append(task['completed'])
            list.append(task['title'])
            write.writerow(list)
