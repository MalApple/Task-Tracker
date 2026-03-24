#A command line interface (CLI) to track what I need to do, what I have done, and what I am currently working on. 
import sys
from datetime import datetime
import json
import os

FILE = "tasks.json"

#Loads JSON file and creates new one if not found
def load_task():
    if not os.path.exists(FILE):
        return []
    
    with open(FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            return []

#Opens FILE in write mode and saves the "whole" list
def save_tasks(task):    
    with open(FILE, 'w') as f:
        json.dump(task, f, indent = 4)


#Function that handles user inputs
def userInput():

    command = sys.argv[1]

    ##Basic add and delete user input cases##
    if command == "add":
        new_task = {
            "id": len(to_do) + 1,
            "description": sys.argv[2],
            "status": "to do",
            "created_at": str(datetime.now()),
            "updated_at": str(datetime.now())
        }
        
        to_do.append(new_task)
        save_tasks(to_do)

        print(f"Added: {sys.argv[2]}")

        #Debug
        # print(f"id: {new_task['id']}\n"
        #       f"Description: {new_task['description']}\n"
        #       f"Status: {new_task['status']}\n"
        #       f"Date Created: {new_task['created_at']}\n"
        #       f"Date Updated: {new_task['updated_at']}\n")

    elif command == "delete":
        for task in to_do:
            if task["id"] == int(sys.argv[2]):
                to_do.remove(task)
                save_tasks(to_do)

                print("Task deleted")
                return
            
        print("Task can not be found")      

    elif command == "clearlist":
        print("Do you wish to delete the whole list? Y/N?")
        if input() == 'Y':
            os.remove("tasks.json")
            print("List deleted")
        elif input() == 'N':
            return
        else:
            print("Did not enter a valid reply")

    ##User inputs relating to maintaining the todo list##
    elif command == "update":
        for task in to_do:
            if task["id"] == int(sys.argv[2]):
                task["description"] = sys.argv[3]
                task["updatede_at"] = str(datetime.now())
                save_tasks(to_do)

                print(f"Updated task to: {sys.argv[3]}")
                return
            
        print("Task can not be found")

    elif command == "list":
        if len(sys.argv) <= 2:
            for task in to_do:
                print(f"Task {task['id']}: {task['description']} [{task['status']}]")
            return

        filter_status = sys.argv[2]

        for task in to_do:
            if task["status"] == filter_status:
                print(f"Task {task['id']}: {task['description']} [{task['status']}]")


    elif command == "mark-in-progress":
        for task in to_do:
            if task["id"] == int(sys.argv[2]):
                task["status"] = "in-progress"
                save_tasks(to_do)

    elif command == "mark-done":
        for task in to_do:
            if task["id"] == int(sys.argv[2]):
                task["status"] = "done"
                save_tasks(to_do)


to_do = load_task()
userInput()