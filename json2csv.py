#!/usr/bin/env python3

import re
import csv
import json
import time


out = csv.writer(open("teju.csv", "w"))
out.writerow(['url', 'type', 'created', 'image', 'likes', 'comments', 'hashtags', 'text'])

for post in json.load(open('teju.json')):
    p = post.get
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p('time')))
    hashtags = ','.join([ht for ht in re.findall('#(\w+)', p('text', ''))])
    
    row = [
        'https://www.instagram.com/p/' + p('id'),
        p('type'),
        t,
        p('image'),
        p('likes'),
        p('comments'),
        hashtags,
        p('text'),
    ]
    out.writerow(row)
