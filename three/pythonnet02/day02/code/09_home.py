# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:38:01 2018

@author: Administrator
"""

import requests
import re

baeseurl = "https://www.neihan8.com/article/"

headers = {"User-Agent":"Mozilla/5.0"}

index=0
while True:
    if index !=0:
        url = baeseurl+"index_"+str(index)+".html"
        print("index !=0")
    else:
        url = baeseurl+"index.html"
    response = requests.get(url,headers=headers)
    response.encoding="utf-8"
    html = response.text
    #匹配需要的文本内容
    p = 'class="desc">\s+(.*?)</div>'
    ree = re.compile(p,re.S)
    weneed = ree.findall(html)
    print(weneed)
    index +=1
    inputStr = input("y or n>>")
    if inputStr =="n":
        print("quit")
        break
    if inputStr=="y":
        print("contue")
        continue
    
    



