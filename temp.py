# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json

queryjson = []
counter=0;
in_file_path='/home/tanvi/Downloads/Tanvi_Query_1.json' # Change me!

with open(in_file_path,'r') as in_json_file:

    # Read the file and convert it to a dictionary
             json_obj = json.load(in_json_file)
             tweets=json_obj[0]['hits']['hits']
             
             for tweet in tweets:
                 if tweet['_source']['geo_tag'] ==1 :
                     counter+=1
                     queryjson.append(tweet)
        
        
             filename='/home/tanvi/Downloads/geotweets.json'
             with open(filename, 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`
                 json.dump(queryjson, out_json_file, indent=4)
                 
             print(counter)