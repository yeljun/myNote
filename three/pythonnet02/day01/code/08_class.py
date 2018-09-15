# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:26:36 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

class BaiduSpider:
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com/f?"
        self.headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
    #请求并读取页面内容
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html
    #保存文件
    def writePage(self,filename,html):
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html)
    def workOn(self):
        name = input("输入贴吧名>>")
        begin = int(input("输入起始页>>"))
        end = int(input("输入终止页>>"))
        kw= {"kw":name}
        kw = urllib.parse.urlencode(kw)
        for page in range(begin,end+1):
            pn = (page-1)*50
            url = baseurl+kw+"&pn="+str(pn)
            print("正在下载第%d页" % page)
            html = self.getPage(url)
            print("aaa")
            filename = name+"第"+str(page)+"页.html"
            self.writePage(filename,html)
            print("下载成功")
            print("*"*10)

if __name__=="__main__":
    spider = BaiduSpider()
    spider.workOn()
