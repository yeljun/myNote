# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:55:25 2018

@author: Administrator
"""

import requests
import json



word = input("请输入内容")
data = {
     "i":word,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1536648837607",
    "sign":"266521c5f642dc5f23cc525389978775",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION",
    "typoResult":"false",
     }
#把data转为bytes数据类型
#decode()位字符串,encode()为bytes

#发请求
#url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla5.0"}
res = requests.post(url,data=data,headers=headers)
res.encoding="utf-8"
result = res.text
#print(result)
#print(type(result))
#返回的result是JSON格式的字符串
#{"type":"ZH_CN2EN",
#"errorCode":0,
#"elapsedTime":1,
#"translateResult":[[{"src":"你好","tgt":"hello"}]]
#}


#把json格式的字符串转换为Python字典
#json模块中的loads方法：json格式字符串转换成字典
result_dict = json.loads(result)
reu = result_dict["translateResult"][0][0]["tgt"]

print(reu)
