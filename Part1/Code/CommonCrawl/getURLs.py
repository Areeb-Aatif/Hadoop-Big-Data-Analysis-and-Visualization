import requests
import json
import io
import gzip
from bs4 import BeautifulSoup
import csv
import shutil
import urllib
import warc

urlList = []
def search_domain(domain):
    url = "https://index.commoncrawl.org/CC-MAIN-2019-04-index?"
    url += "url=%s&matchType=domain&output=json" % domain
    response = requests.get(url)
    if response.status_code == 200:
        records = response.content.splitlines()
        for record in records:
            rcList = []
            data = json.loads(record)
            rurl = data['url']
            if 'languages' in data:
                lan = data['languages']
                if ("college admission scandal" in rurl or "college admission scam" in rurl
                        or "scam" in rurl or "fraud" in rurl or "college fraud" in rurl) and lan == "eng":
                    rcList.append(data['filename'])
                    rcList.append(data['url'])
                    urlList.append(rcList)

def writeFile():
    with open('ccData1.csv', 'w', encoding='utf-8', newline='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerows(urlList)

domainList = list()
with open('domain.txt', 'r') as f:
   for line in f:
        line=line.strip()
        domainList.append(line)

for domain in domainList:
    search_domain(domain)
writeFile()
