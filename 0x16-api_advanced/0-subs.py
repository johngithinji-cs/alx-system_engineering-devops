#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns total subs"""
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json().get("data", None).get("subscribers", None)
    else:
        return 0

if __name__ == "__main__":
    pass
