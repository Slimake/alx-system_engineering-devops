#!/usr/bin/python3
"""
0-subs Module
"""
import requests


def number_of_subscribers(subreddit):
    """
    return numbers of subscribers for a subreddit or
    return 0 if subreddit given doesn't exist
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = requests.utils.default_headers()
    headers.update({"User-Agent": "api/v1"})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
