import argparse
import urllib.request
import json

def api_search(username):
    
    try:
        response = urllib.request.urlopen(f"https://api.github.com/users/{username}/events")
    
    except urllib.error.HTTPError as http:
        print(f"Error! Status Code: {http.code}")
        return
    
    content = response.read().decode('utf-8')
    data = json.loads(content)
    with open("activity.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("activity.json", "r") as f:
        data = json.load(f)

    events = {
        "CommitCommentEvent" : 0,
        "CreateEvent" : 0,
        "DeleteEvent" : 0,
        "DiscussionEvent" : 0,
        "ForkEvent" : 0,
        "GollumEvent" : 0,
        "IssueCommentEvent" : 0,
        "IssuesEvent" : 0,
        "MemberEvent" : 0,
        "PublicEvent" : 0,
        "PullRequestEvent" : 0,
        "PullRequestReviewEvent" : 0,
        "PullRequestReviewCommentEvent" : 0,
        "PushEvent" : 0,
        "ReleaseEvent" : 0,
        "WatchEvent" : 0}

    push_event = {}

    for item in data:
        if item["type"] == "PushEvent":
            if item["repo"]["name"] not in push_event:
                push_event.update({item["repo"]["name"] : 1})
            else:
                push_event[item["repo"]["name"]] += 1

        if item["type"] == "CreateEvent":
            repo = item["repo"]["name"]
            created = item["payload"]["ref"]
            created_type = item["payload"]["ref_type"]
            
            if created is not None:
                print(f"Created a {created_type} '{created}' in {repo}")
            else:
                print(f"Created a repository {repo}")

        events[item["type"]] += 1

    if push_event != {}:
        for push in push_event:
            print(f"Pushed {push_event[push]} commits to {push}")

    print(events)

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity CLI")
    parser.add_argument("username", type=str)
    username = parser.parse_args().username

    api_search(username)

if __name__ == "__main__":
    main()