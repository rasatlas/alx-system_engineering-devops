#!/usr/bin/python3
"""A function that queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '/u/myuseragent'}

    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        total_subscribers = data['data']['subscribers']
        return total_subscribers
    else:
        return 0
