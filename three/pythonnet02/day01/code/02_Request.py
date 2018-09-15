# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:18:13 2018

@author: Administrator
"""
import urllib.request

url = "https://www.baidu.com"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}


#构建请求对象
request = urllib.request.Request(url,headers=headers)
#获取响应对象
response = urllib.request.urlopen(request)
#获取响应对象的内容
html =response.read().decode("utf-8")

print(html)


