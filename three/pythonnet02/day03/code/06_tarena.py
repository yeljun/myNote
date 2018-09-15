# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:57:19 2018

@author: Administrator
"""

import requests
import re

class Note:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla5.0/"}
        #auth是元组参数
        self.auth = ("tarenacode","code_2013")
        self.url ="http://code.tarena.com.cn/"
    def getParsePage(self):
        res = requests.get(self.url,auth=self.auth,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        p = re.compile('a href="\w+/">(.*?)</a>',re.S)
        r_list = p.findall(html)
        self.savePage(r_list)
    def savePage(self,r_list):
        print("开始写入")
        for r_str in r_list:
            with open("danei.txt","a") as f:
                f.write(r_str+"\n")
        print("写入完成")
if __name__=="__main__":
    note = Note()
    note.getParsePage()