#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests

USER_AGENT = "linux:alu.api_advanced:v1.0.0 (by /u/alu_student)"


def print_counts(counts, word_list):
    """Print the keyword totals sorted by count, then alphabetically."""
    words = [word.lower() for word in word_list]
    totals = {}
    for word in set(words):
        total = counts.get(word, 0) * words.count(word)
        if total > 0:
            totals[word] = total
    ordered = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    for word, total in ordered:
        print("{}: {}".format(word, total))


def count_words(subreddit, word_list, counts=None, after=None):
    """Recursively count the keywords of word_list in hot post titles."""
    if counts is None:
        counts = {}
    if subreddit is None or not isinstance(subreddit, str):
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        params={"after": after, "limit": 100},
        allow_redirects=False,
    )
    if response.status_code != 200:
        print_counts(counts, word_list)
        return
    data = response.json().get("data", {})
    wanted = [word.lower() for word in word_list]
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in wanted:
                counts[token] = counts.get(token, 0) + 1
    after = data.get("after")
    if after is None:
        print_counts(counts, word_list)
        return
    count_words(subreddit, word_list, counts, after)
