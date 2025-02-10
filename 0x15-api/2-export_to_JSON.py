#!/usr/bin/python3
"""Script to export employee task data in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    # Validate input
    try:
        employee_id = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} employee_id")
        sys.exit(1)

    # Fetch user information
    user_url = f"{base_url}users/{employee_id}"
    response = requests.get(user_url)
    
    if response.status_code != 200:
        print("Error: User not found")
        sys.exit(1)
    
    user = response.json()
    user_name = user.get('username')

    # Fetch tasks
    tasks_url = f"{base_url}todos?userId={employee_id}"
    response = requests.get(tasks_url)
    
    if response.status_code != 200:
        print("Error: Failed to fetch tasks")
        sys.exit(1)
    
    tasks = response.json()
    
    # Build JSON structure
    user_data = {employee_id: [
        {"task": task["title"], "completed": task["completed"], "username": user_name}
        for task in tasks
    ]}

    # Write JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(user_data, json_file, indent=4)
