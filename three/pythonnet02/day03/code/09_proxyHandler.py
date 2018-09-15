# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:03:51 2018

@author: Administrator
"""

import urllib.request

url = "http://www.baidu.com/"
proxy={"HTTP":"111.226.188.37:8010"}
#1创建handler
proxy_handler = urllib.request.ProxyHandler(proxy)
#2创建自定义opener
opener = urllib.request.build_opener(proxy_handler)
#利用open发送请求
req =urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))


