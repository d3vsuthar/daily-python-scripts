import requests
import xml.etree.ElementTree as ET
import sys

if sys.argv[1]:
  recent_n = int(sys.argv[1])
else:
  recent_n = 10

url = "https://timesofindia.indiatimes.com/rssfeedmostrecent.cms"

res = requests.get(url)

root = ET.fromstring(res.content)

# create empty list for news items
newsitems = []

# iterate news items
for item in root.findall('./channel/item'):

    # empty news dictionary
    news = {}

    # iterate child elements of item
    for child in item:

        news[child.tag] = child.text

    newsitems.append(news)


for x in newsitems[:recent_n]:
    print(f"{x['pubDate']} - {x['title']}")
    print(x['link'], "\n")
