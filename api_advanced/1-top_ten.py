#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, print None."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(json_data.get('data').get('children')[i].get('data').get('title'))
    else:
        print(None)  # Handle both non-existent and other errors

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: ./script.py <subreddit>")
