from bs4 import BeautifulSoup
import requests


def get_static_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find(id='mw-content-text')
    [s.extract() for s in content('table', {'class':'infobox'})]
    return content.get_text()[:750]

import requests
from readability import Document


def get_readable(url):
  response = requests.get(url)
  doc = Document(response.content)
  doc.title()
  return doc.summary()

url = "https://edition.cnn.com/2023/08/21/travel/jetzero-blended-wing-plane-climate-spc/index.html"
print (get_readable(url))