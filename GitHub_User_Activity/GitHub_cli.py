#A command line interface to fetch user activity from github, displaying recent activity with time and date
import sys
import json
from urllib import request, error
from datetime import datetime
from datetime import timezone
from zoneinfo import ZoneInfo

def userInput() -> str:
    user_name = sys.argv[1]
    return user_name

def buildURL(user_name) -> str:
    url = f"https://api.github.com/users/{user_name}/events"
    return url

def fetchData(url) -> dict:
    try:
        response = request.urlopen(url)
        data = response.read()
        events = json.loads(data)
        return events
    
    except error.HTTPError as e:
        if e.code == 404:
            print("Error: User not found")
        else:
            print("Error: {e.code}") 
        return None
    
    except error.URLError:
        print("Error: Failed to connect to GitHub")
        return None

def formatTime(raw_time) -> str:
    dt = datetime.strptime(raw_time, "%Y-%m-%dT%H:%M:%SZ")
    dt = dt.replace(tzinfo=timezone.utc)
    sa_time = dt.astimezone(ZoneInfo("Australia/Adelaide"))
    time = sa_time.strftime("%d %b %Y, %I:%M %p")
    return time

def outputData(events):
    for event in events[:5]:
        repo = event['repo']['name']
        payload = event.get('payload', {})
        time = formatTime(event['created_at'])

        if event['type'] == 'PushEvent':
            commits = payload.get('commits')
            if commits:
                print(f"- Pushed {len(commits)} commits to {repo} ({time})")
            else:
                ref = payload.get('ref', '')
                branch = ref.split('/')[-1] if ref else "unknown branch"
                print(f"- Pushed to {repo} on {branch} ({time})")

        elif event['type'] == 'WatchEvent':
            print(f"- Starred {repo} ({time})")

        elif event['type'] == 'ForkEvent':
            print(f"- Forked {repo} ({time})")

        elif event['type'] == 'IssuesEvent':
            action = payload.get('action', 'updated')
            print(f"- {action.capitalize()} an issue in {repo} ({time})")

        elif event['type'] == 'IssueCommentEvent':
            print(f"- Commented on an issue in {repo} ({time})")

        elif event['type'] == 'PullRequestEvent':
            action = payload.get('action', 'updated')
            print(f"- {action.capitalize()} a pull request in {repo} ({time})")

        elif event['type'] == 'PullRequestReviewEvent':
            print(f"- Reviewed a pull request in {repo} ({time})")

        elif event['type'] == 'PullRequestReviewCommentEvent':
            print(f"- Commented on a pull request in {repo} ({time})")

        elif event['type'] == 'CreateEvent':
            ref_type = payload.get('ref_type', 'something')
            print(f"- Created a {ref_type} in {repo} ({time})")

        elif event['type'] == 'DeleteEvent':
            ref_type = payload.get('ref_type', 'something')
            print(f"- Deleted a {ref_type} in {repo} ({time})")

        elif event['type'] == 'PublicEvent':
            print(f"- Made {repo} public ({time})")

        else:
            print(f"- Did {event['type']} on {repo} ({time})")



def main():
    user_name = userInput()
    url = buildURL(user_name)
    events = fetchData(url)

    if events:
        outputData(events)
    else:
        print("No events found")


if __name__ == "__main__":
    main()



    