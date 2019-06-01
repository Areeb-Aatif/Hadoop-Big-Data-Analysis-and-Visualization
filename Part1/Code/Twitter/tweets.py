import tweepy as tp
import json
import datetime
import re, csv

ConsumerKey = ''
ConsumerSecret = ''
AccessToken = ''
AccessSecret = ''

auth = tp.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessSecret)
api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

querylist = list()
with open('keywords.txt', 'r') as queryfile1:
   for line in queryfile1:
        line=line.strip()
        querylist.append(line)

geolist = list()
with open('geo.txt', 'r') as geofile:
   for line in geofile:
        line=line.strip()
        geolist.append(line)

with open('tweets4.csv', 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    count = 0
    for word in querylist:
        result = tp.Cursor(api.search, q=word + '-filter:retweets', geocode='38.358984,-98.590597,1000mi', lang='en', tweet_mode='extended', count=100).items(200000)
        tweets = []
        for tweet in result:
            data = []
            if tweet.place:
                if tweet.place.country_code == "US":
                    data.append(tweet._json['created_at'])
                    data.append(tweet._json['id'])
                    data.append(tweet._json['full_text'])
                    tweets.append(data)
                    count = count + 1
        print(count)
        writer.writerows(tweets)
output.close()
