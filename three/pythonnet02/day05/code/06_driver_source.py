# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:11:40 2018

@author: Administrator
"""

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

#1---
#req = driver.page_source.find("kw")
#re  = driver.page_source.find("laok")
#print(req)
#print(re)


#2----
rest = driver.find_element_by_id("setf").text
print(rest)



