#!/usr/bin/python3
"""Script to fetch and display an employee's TODO list progress from an API."""
import requests
import sys

if __name__ == "__main__":
    # Validate input
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch employee details
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error: Employee ID not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch employee tasks
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]

    # Display result
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

