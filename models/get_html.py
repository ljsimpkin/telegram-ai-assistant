from bs4 import BeautifulSoup
import requests
from readability import Document


def get_static_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find(id='mw-content-text')
    [s.extract() for s in content('table', {'class':'infobox'})]
    return content.get_text()[:750]


def parse_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()


import re

def clean_text(text):
    text = re.sub(r'\n+', '\n', text)  # remove multiple new lines
    text = re.sub(r'\[\d+\]', '', text)  # remove references like [1], [2], etc.
    return text.strip()  # remove leading and trailing whitespace

def get_readable(url):
  response = requests.get(url)
  doc = Document(response.content)
  doc.title()
  summary_html = doc.summary()
  return clean_text(parse_html_to_text(summary_html))

url = "https://edition.cnn.com/2023/08/21/travel/jetzero-blended-wing-plane-climate-spc/index.html"
# url = "https://en.wikipedia.org/wiki/New_Zealand"
print (get_readable(url))
