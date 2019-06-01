import requests
import json
import io
import gzip
from bs4 import BeautifulSoup
import csv
import shutil
import urllib
import warc

urlList = list()
data = list()
with open('ccUrl1.csv', 'r') as f:
   for line in f:
        line = line.strip()
        url, furl = line.split(',', 1)
        urlList.append(furl)

for url in urlList:
    article = []
    article.append(url)
    resp = requests.get(url)
    parsedHTML = BeautifulSoup(resp.text, "html.parser")

    text = ""
    for para in parsedHTML.find_all('p'):
        text += para.text.strip()
    article.append(text)
    data.append(article)

with open('ccData1.csv', 'a', encoding='utf-8', newline='') as outputFile:
        writer = csv.writer(outputFile, delimiter=',')
        writer.writerows(data)
                    