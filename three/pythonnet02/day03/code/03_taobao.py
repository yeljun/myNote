# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:54:09 2018

@author: Administrator
"""

import requests

url ="http://www.taobao.com/"
proxies = {"http":"125.118.148.188:808"}
headers = {"User-Agent":"Mozilla5.0"}
res = requests.get(url,proxies=proxies,headers=headers)
res.encoding="utf-8"
print(res.text)