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
    text = re.sub(r'\t', '', text)  # remove tabs
    text = re.sub(r'  ', '', text)  # replace double spaces with nothing
    return text.strip()  # remove leading and trailing whitespace

def get_readable(url):
  response = requests.get(url)
  doc = Document(response.content)
  doc.title()
  summary_html = doc.summary()
  return clean_text(parse_html_to_text(summary_html))

# url = "https://edition.cnn.com/2023/08/21/travel/jetzero-blended-wing-plane-climate-spc/index.html"
# url = "https://en.wikipedia.org/wiki/New_Zealand"
# url = "https://www.technologyreview.com/2023/08/18/1077537/menstruation-mystery/"
# url = "https://www.economist.com/finance-and-economics/2023/08/24/chinas-economy-is-in-desperate-need-of-rescue"
url = "https://www.technologyreview.com/2023/08/18/1077548/computer-waste-heat/"
print (get_readable(url))