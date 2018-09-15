# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:34:46 2018

@author: Administrator
"""
import urllib.request

url = "http://www.baidu.com/"

headers = "User-Agent:Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
request =urllib.request.Request(url)
request.add_header("User-Agent",headers)
#获取响应对象
response = urllib.request.urlopen(request)
#get_header()获取User-Agent
print(request.get_header("User-agent"))
#获取响应码
print(response.getcode())
#获取响应报头信息
print(response.info())

