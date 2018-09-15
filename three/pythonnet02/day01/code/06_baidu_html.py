# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:08:31 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

baseurl = "https://tieba.baidu.com/f?"
headers = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}

name = input("贴吧名>>")
begin = int(input("请输入起始页>>"))
end = int(input("请输入终止页>>"))

#url进行编码
kw = {"kw":name}
kw = urllib.parse.urlencode(kw)

#写循环拼接url，发请求获取响应，写入本地文件
for page in range(begin,end+1):
    #拼接url
    pn=(page-1)*50
    url = baseurl + kw +"&pn="+str(pn)
    #print(url)
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8") #字符串
    #写文件保存到本地
    filename = "第"+str(page)+"页.html"
    print("url-->>>",url)
    with open(filename,"w",encoding="utf-8") as f:
        print("正在下载第%d页" % page)
        f.write(html)
        print("文件下载成功")
        print("*"*30)
    






