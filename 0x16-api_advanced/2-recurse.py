#!/usr/bin/python3
"""A recursive function that queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    A recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit.
    If no results are found for the given subreddit, the function
    should return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 9}
    headers = {"User-Agent": "/u/guest"}

    resp = requests.get(url,
                        headers=headers,
                        params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        return None

    data = resp.json()
    hot_posts = data['data']['children']
    if len(hot_posts) == 0:
        return
    else:
        hot_list.append(hot_posts[0]['data']['title'])
        hot_posts.pop(0)
    after = data['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
