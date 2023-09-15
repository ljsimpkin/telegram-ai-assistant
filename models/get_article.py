from bs4 import BeautifulSoup
import requests
from readability import Document
import re

def parse_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

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
# url = "https://www.technologyreview.com/2023/08/18/1077548/computer-waste-heat/"

url = "http://www.nytimes.com/2009/12/21/us/21storm.html"
# print (get_readable(url))


# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import urllib.request

# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True

# # This implimentation works to get more text however it gets extra text like javascript is not enabled etc. Enabling javascript may help using playwright

# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)
#     clean_texts=clean_text(u" ".join(t.strip() for t in visible_texts))  
#     return clean_texts

# html = urllib.request.urlopen(url).read()
# print(text_from_html(html))