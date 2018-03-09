#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 10:54
# @Author  : Peng Y.
# @Site    : 
# @File    : QiuBai_XPath.py
# @Software: PyCharm


import requests
import re
import time
import random
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}


def getInfo(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        html = etree.HTML(res.text)
#        ID = html.xpath('//*[@id="content-left"]//h2/text()')
#        Text = html.xpath('//*[@id="content-left"]//a / div / span/text()')
#        Up = html.xpath('//*[@id="content-left"]//div/span/i/text()')
#        Comment  = html.xpath('//*[@id="content-left"]//div/span/a/i/text()')
#
#        texts = []
#        for id,text,up,comment in zip(ID,Text,Up,Comment):
#            texts.append([id,text,up,comment])



        texts = html.xpath('//*[@id="content-left"]//div/span/a/i/text()|//*[@id="content-left"]//a / div / span/text()|//*[@id="content-left"]//div/span/i/text()|//*[@id="content-left"]//div/span/a/i/text()')

        return texts
    else:
        pass

def dumpToFile(text):
    pass

if __name__ == "__main__":
    Input = 2 #int(input('Please Input Pages ------'))
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,Input)]
    for url in urls:
        text = getInfo(url)
        print(text)
        #for  i in text:
        #    print(i)
        #    print("\n"*2)
#            for j in i:
#                print(j[0].strip('\n'),j[1].strip('\n'),j[2].strip('\n'),j[3].strip('\n'))



