# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:12:48 2018

@author: Administrator
"""
import requests
import re

class Neihan:
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/article/"
        self.headers={"User-Agent":"Mozilla5.0/"}
        self.index=1
        
    def getPage(self,url):
        res= requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html = res.text
        
        self.parsePage(html)
    def parsePage(self,html):
        zz = 'class="desc">\s+(.*?)</div>'
        p = re.compile(zz,re.S)
        r_list= p.findall(html)
        
        self.savePage(r_list)
    def savePage(self,r_list):
        
        
        for r_str in r_list:
            r_str.replace("\u3000","")
            print(r_str,">>>>>>>>")
            
            with open("neihan.txt","a",encoding="utf-8") as f:
                f.write(r_str+"\n\n")
        
    def workOn(self):
        while True:
            if self.index==1:
                url =self.baseurl+"index.html"
            else:
                url = self.baseurl+"index_"+str(self.index)+".html"
            print("正在获取网页")
            self.getPage(url)
            inputStr = input("y or n>>>")
            if inputStr =="n":
                print("退出")
                break
            else:
                self.index+=1
                continue
if __name__=="__main__":
    neihan = Neihan()
    neihan.workOn()
