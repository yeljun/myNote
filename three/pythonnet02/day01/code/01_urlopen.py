# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import urllib.request

url = "http://www.baidu.com/"
#发起请求，接收响应
response = urllib.request.urlopen(url)
#响应对象的read方法获取响应的内容
#read()得到的是byts类型
#decode() bytes  -->  string
html = response.read().decode("utf-8")
print(html)
print(type(html))