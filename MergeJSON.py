#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:25:13 2018

@author: tanvi
"""
import json
import glob
glob_data = []
for file in glob.glob('/home/tanvi/Documents/files/Tweets*.json'):
    with open(file) as json_file:
        print(json_file.name)
        data = json.load(json_file)
        i = 0
        while i < len(data):
            glob_data.append(data[i])
            i += 1
    
    with open('/home/tanvi/Documents/files/mergedTweetsFile.json', 'w') as f:
        json.dump(glob_data, f, indent=4)
        print('file written')
#list1= '/home/tanvi/Documents/files/tweets1.json'
#list2= '/home/tanvi/Documents/files/tweets2.json'
#
#with open(list1) as file:
#    tweets_data1 = json.loads(file.read())
#
#with open(list2) as file:
#    tweets_data2 = json.loads(file.read())
#
#res_dict = tweets_data1 + tweets_data2
#
#with open('/home/tanvi/Documents/files/mergedfile.json', 'w') as f:
#    json.dump(res_dict, f, indent=4)
#    print('file written')