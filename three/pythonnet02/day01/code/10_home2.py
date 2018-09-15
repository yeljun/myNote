# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:57:30 2018

@author: Administrator
"""
import urllib.request
import urllib.parse


class Maoyan:
    def __init__(self):
        self.baseurl = "http://www.maoyan.com/board/4?offset="
        self.headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
    def getPage(self,number):
        url = self.baseurl+str(number)
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html
    def writePage(self,filename,html):
        with open(filename,"a",encoding="utf-8") as f:
            f.write(html)
    def workOn(self):
        
        number = 0
        while True:
            inputStr = input("输入字符'y'or'n'>>")
            if inputStr=="n":
                print("欢迎下次光临")
                break
            if inputStr=="y":
                print("稍等，正在努力下载中...")
            html = self.getPage(number)
            print("正在保存文件")
            filename = "maoyan_第"+str(int(number/10))+"页.html"
            self.writePage(filename,html)
            print("你可以使用了")
            print("*"*10)
            number+=10
            
            

if __name__=="__main__":
    maoyan=Maoyan()
    maoyan.workOn()