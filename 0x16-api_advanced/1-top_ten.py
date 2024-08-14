#!/usr/bin/python3
"""
1-top_ten Module
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    prints the titles of the first 10 hot posts listed
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/new.json"

    headers = {"User-Agent": "api/v1"}
    params = {"limit": "9"}

    r = requests.get(url, headers=headers, params=params).json()
    hot_posts = r.get('data', {}).get('children')
    if not hot_posts:
        print(None)
    else:
        for post in hot_posts:
            print(post.get('data').get('title'))
