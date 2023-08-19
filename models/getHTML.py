import requests


def get_static_website(url):
    response = requests.get(url)
    return response.text
