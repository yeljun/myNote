# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:54:03 2018

@author: Administrator
"""

import urllib.request

url = "http://www.baidu.com/"
#创建HTTPHandler处理器对象
http_handler = urllib.request.HTTPHandler()
#创建自定义的opener对象
opener = urllib.request.build_opener(http_handler)
#3利用opener对象的open方法发送请求
req = urllib.request.Request(url)

res = opener.open(req)
print(res.read().decode("utf-8"))