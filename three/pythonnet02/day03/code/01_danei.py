# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:20:44 2018

@author: Administrator
"""
import requests

url = "http://www.baidu.com/s?"
headers = {"User-Agent":"Mozilla5.0/"}

s = input("kw>>")
#get方法params参数必须要为字典格式
wd = {"wd":s}
res = requests.get(url,params=wd,headers=headers)
res.encoding="utf-8"
print(res.text)