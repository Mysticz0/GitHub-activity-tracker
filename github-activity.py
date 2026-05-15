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

        if item["type"] == "PublicEvent":
            repo = item["repo"]["name"]
            print(f"Made repository '{repo}' public")

        if item["type"] == "PullRequestEvent":
            repo = item["repo"]["name"]
            pull_request_action = item["payload"]["action"].capitalize()
            pull_request_name = item["payload"]["pull_request"]["head"]["ref"]
            
            print(f"{pull_request_action} a pull request '{pull_request_name}' in {repo}")

    if push_event != {}:
        for push in push_event:
            print(f"Pushed {push_event[push]} commits to {push}")

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity CLI")
    parser.add_argument("username", type=str)
    username = parser.parse_args().username

    api_search(username)

if __name__ == "__main__":
    main()