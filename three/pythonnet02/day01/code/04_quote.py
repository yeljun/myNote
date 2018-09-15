# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:03:37 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
url = 'http://www.baidu.com/s?wd='
key = input("请输入要搜索的内容")
#编码拼接url
key = urllib.parse.quote(key)
fullurl = url+key
#构建请求对象
request = urllib.request.Request(fullurl,headers=headers)
#获取响应对象
response = urllib.request.urlopen(request)
#read（）decode()
html = response.read().decode("utf-8")
print(html)
