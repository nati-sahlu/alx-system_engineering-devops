#!/usr/bin/python3
"""Script to fetch an employee's TODO list progress and export to CSV."""
import csv
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
    username = user.get("username")

    # Fetch employee tasks
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Write to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task.get("completed"), task.get("title")])

    print(f"Data exported to {filename}")

