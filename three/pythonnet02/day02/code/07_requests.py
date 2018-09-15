# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:54:34 2018

@author: Administrator
"""

import requests

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla5.0/"}
response = requests.get(url,headers=headers)
print(response.encoding)
#ISO-8859-1
response.encoding="utf-8"

#print("aaa",response.text)
#print(response.content)
print(response.status_code)






