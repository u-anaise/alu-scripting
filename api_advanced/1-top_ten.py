#!/usr/bin/python3
"""Module that prints the first 10 hot post titles of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
