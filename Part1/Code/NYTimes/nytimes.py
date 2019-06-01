import requests
import json
from bs4 import BeautifulSoup
import csv
import time

nyTimesAPIKey = "API_KEY"
def parse_json(data, nyData):
    for doc in data['response']['docs']:
        article = []
        article.append(doc['web_url'])
        resp = requests.get(doc['web_url'])
        time.sleep(10)
        parsedHTML = BeautifulSoup(resp.text, "html.parser")

        text = ""
        for para in parsedHTML.find_all('p', class_='evys1bk0'):
            text += para.text
        article.append(text)
        nyData.append(article)

def writeFile(page, nyData):
    page = 8 + page
    with open('nyData4(page'+str(page)+').csv', 'a', encoding='utf-8', newline='') as outputFile:
        writer = csv.writer(outputFile, delimiter=',')
        writer.writerows(nyData)

for i in range(0, 5):
    nyData = []
    response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?q=murder&begin_date=20190101&page="+str(i)+"&fq=news_desk=U.S.&api-key="+nyTimesAPIKey)

    data = response.json()
    parse_json(data, nyData)
    writeFile(i, nyData)
