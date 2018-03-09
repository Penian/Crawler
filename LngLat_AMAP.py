#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 15:12
# @Author  : Peng Y.
# @Site    : 
# @File    : AMAP.py
# @Software: PyCharm
import requests
import pprint
import json




def geocode(address):

    parameters = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(base, parameters)

    jsonDate = json.loads(res.text)
    pprint.pprint(jsonDate)

    answer = res.json()
    print(answer)
    #print(address + "的经纬度：", answer['geocodes'][0]['location'])

if __name__== '__main__':
    #address = input("请输入地址:")
    address = '安庆市'
    geocode(address)
