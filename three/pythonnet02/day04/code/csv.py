# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:16:42 2018

@author: Administrator
"""

import csv

with open("cc.csv","a",newline="") as f:
    writer =csv.writer(f)
    writer.writerow(["id","name","age"])
    writer.writerow(["1","lucy","12"])
    writer.writerow(["2","lulu","11"])
    writer.writerow(["3","momo","10"])
    writer.writerow(["4","dangdang","9"])