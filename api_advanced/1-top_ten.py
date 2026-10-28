#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

USER_AGENT = "linux:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        params={"limit": 10},
        allow_redirects=False,
    )
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
