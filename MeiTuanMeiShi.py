#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 8:25
# @Author  : Peng Y.
# @Site    : 
# @File    : MeiTuanMeiShi.py
# @Software: PyCharm

import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

def getInfo(url):
    res = requests.get(url,headers = headers)
    #print(res.encoding)
    #res.encoding = res.apparent_encoding
    if res.status_code == 200:
        #print(res.text)
        html = etree.HTML(res.text)
        #print(etree.tostring(html))
        where = html.xpath('//li[@class="clear btm"]')
        print(where)
        texts =html.xpath('//div/a[@href]/text()')
        return texts
    else:
        pass


def writeToFile(text):
    pass

if __name__ == "__main__":
    url = 'http://anqing.meituan.com/meishi/b14001/'
    texts = getInfo(url)
    print(texts)
    #writeToFile(texts)

