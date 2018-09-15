# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:59:34 2018

@author: Administrator
"""

import re
s = "A B C D"
p1 = re.compile(r"\w+\s+\w+")
print(p1.findall(s))
#"A B","C D" 
p2 = re.compile(r"(\w+)\s+\w+")
print(p2.findall(s))
#


#1,整体匹配["A B","C D"]
#2，显示括号中的内容 [('A',B),("C","D")]
p3 = re.compile(r"(\w+)\s(\w+)")
print(p3.findall(s))
