# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:22:36 2018

@author: Administrator
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time


driver = webdriver.PhantomJS()
driver.get("http://www.douyu.com/g_LOL")

driver.save_screenshot("image/douyu_index.png")

#源码

#while True:

while True:
    #创建对象
    html = driver.page_source
    soup = bs(html,"lxml")
    #直接调用方法去查找元素
    #主播名称
    name_list = soup.find_all("span",{"class":"dy-name ellipsis fl"})
    
    #人气
    people_num=soup.find_all("span",{"class":"dy-num fr"})
    
    #name,num是一个对象，get_text()
    for name,num in zip(name_list,people_num):
        print("主播名称",name.get_text(),"\n观众人数",num.get_text())
    if html.find("shark-pager-next shark-pager-disable shark-pager-disable-next")==-1:
        print("ok")
        driver.find_element_by_class_name("shark-pager-next").click()
        time.sleep(4)
    else:
        print("quit")
        driver.quit()
        break
    
    



