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
    return soup.get_text('\n')


def get_readable(url):
  response = requests.get(url)
  doc = Document(response.content)
  doc.title()
  summary_html = doc.summary()
  return parse_html_to_text(summary_html)

url = "https://edition.cnn.com/2023/08/21/travel/jetzero-blended-wing-plane-climate-spc/index.html"
print (get_readable(url))
