# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:42:11 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

#发请求，得到html：发请求获取响应
def getPage(url):
    headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html
#保存html文件到本地
def writePage(filename,html):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)
#主函数，调用功能和提示
def workOn():
    name = input("输入贴吧名>>")
    begin = int(input("输入起始页>>"))
    end = int(input("输入终止页>>"))
    baseurl = "https://tieba.baidu.com/f?"
    kw= {"kw":name}
    kw = urllib.parse.urlencode(kw)
    for page in range(begin,end+1):
        pn = (page-1)*50
        url = baseurl+kw+"&pn="+str(pn)
        print("正在下载第%d页" % page)
        html = getPage(url)
        print("aaa")
        filename = name+"第"+str(page)+"页.html"
        writePage(filename,html)
        print("下载成功")
        print("*"*10)
if __name__ =="__main__":
    workOn()
