# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:27:30 2018

@author: Administrator
"""
import requests
import json
import csv
url = "https://movie.douban.com/j/chart/top_list?"
dic = {
"type":"11",
"interval_id":"100:90",
"action":"",
"start":"0",
"limit":"100"}
headers = {"User-Agent":"Mozilla5.0/"}
res = requests.get(url,params=params,headers=headers)
res.encoding="utf-8"
html = res.text
list_a = json.loads(html)
#for x in list_a:
#    print(x)
#    print()
with open("douban.csv","a",newline="") as f:
    writer =csv.writer(f)
    for x in list_a:
        rank =x["rank"]
        score = x["score"]
        url =x["cover_url"]
        name = x["title"]
        actors=""
        for y in x["actors"]:
            actors=actors+y+" "
        country = ""
        for y in x["regions"]:
            country=country+y+" "
        types = ""
        for y in x["types"]:
            types=types+y+" "
        writer.writerow([rank,name,types,actors,score,url,country])
print("下载完成")
        
        
