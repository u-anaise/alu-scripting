#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import requests

USER_AGENT = "linux:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        params={"after": after, "limit": 100},
        allow_redirects=False,
    )
    if response.status_code != 200:
        return hot_list or None
    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
