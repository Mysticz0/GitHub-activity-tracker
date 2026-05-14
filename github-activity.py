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

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity CLI")
    parser.add_argument("username", type=str)
    username = parser.parse_args().username

    api_search(username)

if __name__ == "__main__":
    main()