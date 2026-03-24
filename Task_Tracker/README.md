# Task-Tracker
A simple command-line application to track tasks, including what you need to do, what you're currently working on, and what you've completed.

# Features 
-Add, update, and delete tasks
-Mark tasks as:
    to do
    in-progress
    done
-View all tasks or filter by status
-Persistent storage using a local JSON file
-Automatically creates a data file if none exists

# How to use
Add item:
    python task_cli.py add "Task"

Delete item:
    python task_cli.py delete id

Clear list:
    python task_cli.py clearlist

Update item:
    python task_cli.py id "New description"

Change status of item:
    python task_cli.py in-progress
    python task_cli.py mark-done
    
List of items:
    python task_cli.py list
    python task_cli.py list done
    python task_cli.py list in-progress 

# Requirments
Python 3.x