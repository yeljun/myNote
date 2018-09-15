# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:54:03 2018

@author: Administrator
"""
from selenium import webdriver
#操作键盘鼠标
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

driver.find_element_by_id("kw").send_keys(u"美女")
driver.save_screenshot("image/美女.png")
print("ok")
driver.find_element_by_id("su").click()
time.sleep(10)
driver.save_screenshot("image/nv.png")
print("ok1")
