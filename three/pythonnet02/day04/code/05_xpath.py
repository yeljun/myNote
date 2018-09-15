# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:19:06 2018

@author: Administrator
"""
from lxml import etree


html = """<div class="wrapper">
	<i class="iconfont icon-back" id="back"></i>
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
	</ul>
	<i class="iconfont icon-liebiao" id="menu"></i>
</div>"""

#构建解析对象
parseHtml  = etree.HTML(html)
#2，解析对象调用xpath工具
#获取所有的a标签的href属性值

print("***************************")
r_list = parseHtml.xpath("//a/@href")
for x in r_list:
    print(x)
print("***************************")
r_list = parseHtml.xpath("//a[@id='channel']/@href")
for x in r_list:
    print(x)
print("***************************")
r_list = parseHtml.xpath("//li/a/@href")
for x in r_list:
    print(x)

print("###########################")
r_list = parseHtml.xpath("//ul[@id='nav']/li/a/@href")
for x in r_list:
    print(x)

#获取所有a节点里面的文本内容

r_list = parseHtml.xpath("//a")
print(r_list)
for i in r_list:
    print(i.text)

print("%%%%%%%%%%%%%%%%%")
r_list = parseHtml.xpath("//li/a")
r_list = parseHtml.xpath("//ul[@id='nav']//a")
print(r_list)
for i in r_list:
    print(i.text)
print("%%%%%%%")
r_list = parseHtml.xpath("//a[@id='channel']")

print(r_list)
for i in r_list:
    print(i.text)







