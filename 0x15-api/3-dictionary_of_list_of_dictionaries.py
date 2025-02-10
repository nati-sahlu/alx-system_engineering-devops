import json
import requests

def fetch_todos_and_users():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    
    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data")
        return
    
    users = users_response.json()
    todos = todos_response.json()
    
    user_data = {user["id"]: user["username"] for user in users}
    
    todos_dict = {}
    for todo in todos:
        user_id = todo["userId"]
        if user_id not in todos_dict:
            todos_dict[user_id] = []
        
        todos_dict[user_id].append({
            "username": user_data[user_id],
            "task": todo["title"],
            "completed": todo["completed"]
        })
    
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todos_dict, json_file, indent=4)
    
    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    fetch_todos_and_users()

