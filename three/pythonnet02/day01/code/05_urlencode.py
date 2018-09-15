# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:46:14 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

baseurl = "http://www.baidu.com/s?"
headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}

key =input(">>>>")
d = {"wd":key}
d = urllib.parse.urlencode(d)
url = baseurl + d
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html  = response.read().decode()
print(html)







