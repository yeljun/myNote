# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:51:07 2018

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#创建phantomjs浏览器对象
driver = webdriver.PhantomJS()

driver.get("https://www.douban.com/")
driver.save_screenshot("image/douban.png")

driver.find_element_by_name("form_email").send_keys("986745717@qq.com")
driver.find_element_by_name("form_password").send_keys("zxcvbnm")
key =input("验证码>>")
driver.find_element_by_id("captcha_field").send_keys(key)
driver.find_element_by_class_name("bn-submit").click()
driver.save_screenshot("image/ok.png")
driver.quit()

