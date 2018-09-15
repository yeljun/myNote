# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:35:35 2018

@author: Administrator
"""

import requests
from lxml import etree

class Tieba:
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com"
        self.headers = {"User-Agent":"Mozilla5.0/"}
#        self.pg=(page-1)*50
        self.index = 1
    def getPageUrl(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html = res.text
        #创建解析对象
        #print("html>>",html)
        parseHtml = etree.HTML(html)
        t_list = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        #['/p/1231412','/p/234252']
        
        for t in t_list:
            t_url = self.baseurl+t
            self.getImageUrl(t_url)
        
    def getImageUrl(self,t_url):
        print("eee")
        res = requests.get(t_url,headers=self.headers)
        res.encoding ="utf-8"
        html=res.text
        #print(html)
        parseHtml = etree.HTML(html)
        i_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        print(i_list)
        for i in i_list:
            self.writeImage(i)
    def writeImage(self,i):
        
        res = requests.get(i,headers=self.headers)
        res.encoding="utf-8"
        html=res.content
        
        #保存到本地
        filename ="image/"+i[-10:]
        print("正在保存%s文件"%filename)
        with open(filename,"wb") as f:
            f.write(html)
        print("保存完毕")
        
    def workOn(self):
        kw = input("输入要搜索的关键词>>")
        #begin = int(input("起始页>>"))
        #end = int(input("终止页>>"))      
        while True:
            pn = (self.index-1)*50
#            params = {
#                    "kw":kw,
#                    "pn":str(pn)
#                    }
            url = self.baseurl+"/f?kw="+kw+"&pg="+str(pn)
            
            self.getPageUrl(url)
            inputStr = input("y or n>>>")
            if inputStr =="n":
                print("quit")
                break
            if inputStr =="y":
                self.index+=1
                continue
                
if __name__ == "__main__":
    tieba = Tieba()
    tieba.workOn()
