"""
2-recurse Module
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetch and print a list containing
    the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {}
    if after:
        params['after'] = after
    print(params)

    # Make the request to Reddit's API
    headers = {"User-Agent": "api/v1"}
    r = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if r.status_code == 200:
        r = r.json()
        hot_posts = r.get('data', {}).get('children')

        # Print titles of the posts
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        # Check if there are more post to fetch
        after = r.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    elif r.status_code == 404:
        return None
