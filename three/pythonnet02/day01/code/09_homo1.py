# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:06:24 2018 

@author: Administrator
"""
import urllib.request
import urllib.parse

baseurl = "http://www.maoyan.com/board/4?offset="

headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}



number = 0
while True:
    inputStr =input("输入'y'or'n'>>")
    if inputStr =="n":
        print("欢迎下次光临")
        break
    if inputStr =="y":
        print("开始下载！！！请稍等。。。")
        url = baseurl+str(number)   
        req = urllib.request.Request(url,headers=headers)
        res = urllib.request.urlopen(req)
        
        html = res.read().decode("utf-8")
        filename = "maoyan_第"+str(int(number/10))+"页.html"
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html)
        print("下载成功")
        print("*"*10)
        
        number+=10
    


