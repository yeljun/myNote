# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:43:00 2018

@author: Administrator
"""
import re


s = """<div><p>aaaaaaaa,bbbbbb</p></div>
<div><p>cccccccc,dddddd</p></div>
"""
#贪婪
#创建编译对象
p = re.compile(r'<div>.*</div>',re.S)
result = p.findall(s)
print(result)

#非贪婪
p = re.compile(r'<div>.*?</div>',re.S)
result = p.findall(s)
print(result)