# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:41:11 2018

@author: Administrator
"""

import requests

url = "http://5b0988e595225.cdn.sohucs.com/q_70,c_zoom,w_640/images/20180727/377ddfe4ff204ed4b6f6233c0ade1bb9.jpeg"
headers = {"User-Agent":"Mozilla5.0/"}
response = requests.get(url,headers=headers)
data = response.content
with open("王昭君.jpeg","wb") as f:
    f.write(data)

