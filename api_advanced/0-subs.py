#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests

USER_AGENT = "linux:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit, or 0 if invalid."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    if data is None:
        return 0
    return data.get("subscribers", 0)
