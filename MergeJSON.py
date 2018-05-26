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
