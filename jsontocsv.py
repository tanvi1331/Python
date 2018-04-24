# -*- coding: utf-8 -*-
#
import json
from pandas.io.json import json_normalize

with open('E:/geotweet.json') as data_file:    
    data = json.load(data_file) 
    print(data)
uid = []
text = []
name = []
user_id=[]
##
geo = []
coord = []
place = []    
for tweet in data:
    geo_enable = (tweet['tweet_data']['user']['geo_enabled'])
    if geo_enable == 1:
        uid.append(tweet['_id'])
        text.append(tweet['tweet_data']['text'])
        name.append(tweet['tweet_data']['user']['name'])
        user_id.append(tweet['tweet_data']['user']['id_str'])
        geo.append(tweet['tweet_data']['geo'])
        coord.append(tweet['tweet_data']['coordinates'])
        place.append(tweet['tweet_data']['place'])   
      
import pandas as pd
#
df = pd.DataFrame({'ids': uid, 'text': text, 'name': name, 'user_id':user_id,'geo': geo, 'coordinates': coord,'place' : place})
df = json_normalize(data)
df.to_csv("E:/tweetsample.csv", sep=',', encoding='utf-8')

