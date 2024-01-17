#!/usr/bin/python3
"""A function that queries the Reddit API."""
import requests


def top_ten(subreddit):
    """
    A funciton that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    headers = {"User-Agent": "/u/guest"}

    resp = requests.get(url,
                        headers=headers,
                        params=params,
                        allow_redirects=False)
    if (resp.status_code == 200):
        data = resp.json()
        hot_posts = data['data']['children']
        if len(hot_posts) == 0:
            print(None)
        else:
            for post in hot_posts:
                title = post['data']['title']
                print(title)
    else:
        print(None)
        return 0
