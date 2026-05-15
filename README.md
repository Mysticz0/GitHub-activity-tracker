# GitHub User Activity

A simple command-line tool that fetches and displays a GitHub user's recent public activity directly from the GitHub API.

## Features

- Fetch a user's recent public events from the GitHub API
- Display activity in a clean, human-readable format in the terminal
- Supports the following event types:
  - `PushEvent` — aggregates commits pushed per repository
  - `CreateEvent` — repository, branch, and tag creations
  - `PublicEvent` — repositories made public
  - `PullRequestEvent` — pull request actions (opened, closed, etc.)
- Caches the raw API response to `activity.json` for inspection
- Graceful handling of HTTP errors (e.g., invalid usernames)

## Requirements

- Python 3.6+
- No third-party dependencies — uses only the Python standard library (`argparse`, `urllib`, `json`)

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/github-user-activity.git
cd github-user-activity
```

No additional setup is required.

## Usage

Run the script from the command line, passing a GitHub username as an argument:

```bash
python github-activity.py <username>
```

### Example

```bash
python github-activity.py kamranahmedse
```

### Sample Output

```
Created a branch 'feature/new-page' in kamranahmedse/developer-roadmap
Opened a pull request 'feature/new-page' in kamranahmedse/developer-roadmap
Made repository 'kamranahmedse/example-repo' public
Pushed 3 commits to kamranahmedse/developer-roadmap
Pushed 1 commits to kamranahmedse/another-repo
```

## How It Works

1. The script accepts a GitHub username as a CLI argument.
2. It calls the GitHub Events API endpoint: `https://api.github.com/users/<username>/events`.
3. The raw JSON response is saved to `activity.json` for reference.
4. Events are parsed by type and printed in a readable summary.

## Error Handling

If the username does not exist or the GitHub API returns an error, the script prints the HTTP status code and exits gracefully:

```
Error! Status Code: 404
```

## Project Structure

```
github-user-activity/
├── github-activity.py   # Main CLI script
├── activity.json        # Cached API response (generated at runtime)
└── README.md
```

## License

MIT
