import re
import requests

class NeiHan:
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/article/"
        self.page = 1
        self.headers = {"User-Agent": "Mozilla5.0/"}
    
    def getPage(self,url):
        
        print(url)
        res = requests.get(url,headers=self.headers)
        print(res)
        res.encoding='utf-8'
        html = res.text
        print(html)
        self.parsePage(html)

    def parsePage(self,html):
        reg = '<div class="desc">(.*?)</div>'
        p = re.compile(reg,re.S)
        r_list = p.findall(html)
        self.writePage(r_list)
    
    def writePage(self,r_list):
        print(r_list)
        for r_str in r_list:
            with open("内涵段子.text",'a')as f:
                f.write(r_str+'\n\n')

    def workOn(self):
        while True:
            if self.page == 1:
                url = self.baseurl + 'index.html'
            else:
                url = self.baseurl +"index_" + str(self.page)+ '.html'
            print("正在爬取第%d页" % self.page)
            self.getPage(url)
            print("第%d页爬取完成" % self.page)
            c = input("是否继续爬取y/n")
            if c.strip() == 'n':
                print()
                break
            else:
                self.page += 1

if __name__ == "__main__":
    spider = NeiHan()
    spider.workOn()