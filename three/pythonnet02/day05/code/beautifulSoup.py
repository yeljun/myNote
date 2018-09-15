# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:44:03 2018

@author: Administrator
"""

from bs4 import BeautifulSoup

html ="<div>一遇风云便化龙</div>"
soup = BeautifulSoup(html,"lxml")
res = soup.div.string
print(res)