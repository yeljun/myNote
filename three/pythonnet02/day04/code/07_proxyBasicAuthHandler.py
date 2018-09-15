# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:45:53 2018

@author: Administrator
"""
import urllib.request

url = "http://www.baidu.com/"
tarenaurl = "http://code.tarena.com.cn/"

server="114.67.228.126:16819"
user="309435365"
password = "szayclhp"

pwd = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd.add_password(None,server,user,password)
pwd.add_password(None,"127.0.0.1:","tarenacode","code_2013")
proxy_handler = urllib.request.ProxyBasicAuthHandler(pwd)
opener = urllib.request.build_opener(proxy_handler)

req = urllib.request.Request(tarenaurl)
res = opener.open(req)
html = res.read().decode("utf-8")
print(html)
