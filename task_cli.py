import sys
from datetime import datetime

to_do = []

def userInput():

    print(sys.argv)
    command = sys.argv[1]

    if command == "add":
        new_task = {
            "id": len(to_do) + 1,
            "description": sys.argv[2],
            "status": "to do",
            "created_at": str(datetime.now()),
            "updated_at": str(datetime.now())
        }
        
        to_do.append(new_task)
        print(f"Added: {sys.argv[2]}")

        print(f"id: {new_task['id']}\n"
              f"Description: {new_task['description']}\n"
              f"Status: {new_task['status']}\n"
              f"Date Created: {new_task['created_at']}\n"
              f"Date Updated: {new_task['updated_at']}\n")

    elif command == "delete":
        for task in to_do:
            if task["id"] == int(sys.argv[2]):
                del task
                print("Task deleted")
                continue
            
        print("Task can not be found")
        

    elif command == "update":
        for task in to_do:
            if task["id"] == int(sys.argv[2]):
                task["description"] = sys.argv[3]
                print(f"Updated task to: {sys.argv[3]}")
                continue
            
        print("Task can not be found")
        

    return 0

userInput()