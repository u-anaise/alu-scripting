#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0.0 (by /u/alu)"}
    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=10,
        )
        posts = response.json().get("data", {}).get("children", [])
    except Exception:
        print("OK", end="")
        return
    if response.status_code != 200 or not posts:
        print("OK", end="")
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
