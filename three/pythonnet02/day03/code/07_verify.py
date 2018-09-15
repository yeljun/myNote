# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:28:42 2018

@author: Administrator
"""

import requests

url = "http://www.12306.cn/mormhweb/"
headers = {"User-Agent":"Mozilla5.0/"}
res = requests.get(url,verify=False,headers=headers)
res.encoding="utf-8"
print(res.text)