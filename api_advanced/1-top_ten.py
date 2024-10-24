#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests

def top_ten(subreddit):
    """Return the titles of the first 10 hot posts for the given subreddit.
    If the subreddit is not valid, print None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    else:
        print(None)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
