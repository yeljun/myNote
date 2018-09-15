# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:18:22 2018

@author: Administrator
"""

import requests
import re


class Lianjia:
    def __init__(self):
        self.baseurl = "http://wh.lianjia.com/ershoufang/"
        self.headers = {"User-Agent":"Mozilla5.0/"}
        self.proxies = {"HTTP":"http//309435365:szayclhp@114.67.228.126:16819"}
        self.index = 1
    def getPage(self,url):
        '''获取网页信息'''
        res = requests.get(url,proxies=self.proxies,headers=self.headers)
        res.encoding="utf-8"
        html =res.text
        self.rePage(html)
    def rePage(self,html):
        '''正则匹配网页'''
#        data-el="region">阳光100大湖第 </a>
#        zz ='data-el="region(.*?)\s+</a>"'
#        
        zz = '<div class="info clear">.*?data-el="region">(.*?)\s+</a>.*?<div class="totalPrice">.*?<span>(.*?)</span>'
        p = re.compile(zz,re.S)
        r_list=p.findall(html)
        self.writePage(r_list)
    def parsePage(self):
        pass
    def writePage(self,r_list):
        '''保存到本地'''
        for r_tuple in r_list:
            for r_str in r_tuple:
                with open("链家二手房.txt","a") as f:
                    f.write(r_str.strip()+" ")
            with open("链家二手房.txt","a") as f:
                f.write("\n")
    def workOn(self):
        '''主程序'''
        while True:
            print("正在下载%d页" % self.index)
            url = self.baseurl+"pg"+str(self.index)+"/"
            self.getPage(url)
            print("下载成功")
            inputStr = input("y or n>>")
            if inputStr =="n":
                print("quit")
                break
            else:
                
                self.index+=1
                continue
        
if __name__=="__main__":
    lj = Lianjia()
    lj.workOn()


