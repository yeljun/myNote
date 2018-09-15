# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:20:38 2018

@author: Administrator
"""

import requests
import re

class Maoyan:
    def __init__(self):
        #请求对象
        self.headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
        self.page = 1
        self.offset=0
        self.baseurl = "http://www.maoyan.com/board/4?offset="
        self.index=1
        
    def getPage(self,url):
        '''获取源码'''
        res = requests.get(url,headers=self.headers)
        print(res)
        res.encoding="utf-8"
        
        print("ppppp")
        html = res.text
        return html
    def parsePage(self,html):
        '''解析html'''
        #class="name">.*?title="(.*?)" 
#        'class="name">.*?title="(.*?)"\s+data-act.*?class="star">\s+(.*?)\s+</p>.*?class="releasetime">(.*?)</p>'
        
        do_re = 'class="name">.*?title="(.*?)"\s+data-act.*?class="star">\s+(.*?)\s+</p>.*?class="releasetime">(.*?)</p>''class="name">.*?title="(.*?)"\s+data-act.*?class="star">\s+(.*?)\s+</p>.*?class="releasetime">(.*?)</p>'
        p =re.compile(do_re,re.S)
        content_list = p.findall(html)
        print(content_list)
        #[("霸王别姬","张国荣","1993-01-01"),(),()]
        return content_list
    def writeCsv(self,content_list):
        '''保存文件'''
        for m_tuple in content_list:
                try:
                    Index_n = m_tuple[2].strip().index("(")
                    addr =m_tuple[2].strip()[Index_n:]
                except:
                    addr =null
                L =[index,m_tuple[0].strip(),m_tuple[1].strip()[3:],m_tuple[2].strip()[5:9],addr]
        with open("maoyantop100.csv","a",newline="",encoding="gb18030") as f:
            writer = csv.writer(f)
            writer.writerow(L)
                
        f.close()
    def workOn(self):
        '''主函数'''
        while True:
             url = self.baseurl+str(self.offset)
             print("正在下载第%d页"%self.page)
             html = self.getPage(url)
             print("aaa")
             content_list = self.parsePage(html)
             print("content_list",content_list)
             self.writeCsv(content_list)
             print("下载成功。。")
             inputStr = input("是否继续（y or n）>>")
             if inputStr.strip().lower()=="y":
                 self.page+=1
                 self.offset+=10
             else:
                 print("体验结束")
                 break

             

if __name__=="__main__":
    spyder = Maoyan()
    spyder.workOn()





















