import requests


def get_user_followers(url):
    """Get the JSON object from a given user's followers."""
    response = requests.get(url)
    return response.json()

