from bs4 import BeautifulSoup
import requests


def get_static_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find(id='mw-content-text')
    [s.extract() for s in content('table', {'class':'infobox'})]
    return content.get_text()[:750]
