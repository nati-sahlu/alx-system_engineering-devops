#!/usr/bin/python3
""" Script for parsing web data from an API
"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Validate input
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit(1)

    employee_id = sys.argv[1]

    # Fetch user details
    user_url = "{}users/{}".format(base_url, employee_id)
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Invalid Employee ID")
        exit(1)

    user = response.json()
    if not user:
        print("Error: No user found")
        exit(1)

    name = user.get('name', 'Unknown')

    # Fetch user tasks
    tasks_url = "{}todos?userId={}".format(base_url, employee_id)
    response = requests.get(tasks_url)
    todos = response.json()

    completed_tasks = [task for task in todos if task.get('completed')]

    # Print output
    print("Employee {} is done with tasks({}/{}):".format(name, len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

