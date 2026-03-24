# GitHub User Activity CLI
A simple command-line application that fetches and displays a GitHub user's recent activity using the GitHub API.

# Features
-Fetches recent public activity for any GitHub user
-Displays activity in a clean, readable format
-Converts timestamps to South Australia (Adelaide) time
-Handles common errors gracefully:
    Invalid usernames
    Network issues
    Empty activity

# Usage
Run the program from the command line and provide a GitHub username:

python GitHub_cli.py <username>

Example:
    python GitHub_cli.py myUserName

# Requirments
Python 3.9+ (required for zoneinfo)
Have tzdata (windows):   
    pip install tzdata
