# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:36:09 2018

@author: Administrator
"""

#导入selenium库中的webdriver
from selenium import webdriver

#创建打开phantomjs的对象
driver = webdriver.PhantomJS()

#访问百度
driver.get("http://www.baidu.com/")
#获取网页棘突
driver.save_screenshot("baidu.png")