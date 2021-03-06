#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 15:09
# @Author  : Peng Y.
# @Site    : 
# @File    : QiuBai_XPath-2.py
# @Software: PyCharm


import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}



def getInfo(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        html = etree.HTML(res.text)
        #forBlock = html.xpath('//div[starts-with(@class,"article block untagged mb15")]')
        forBlock = html.xpath('//div[@class="article block untagged mb15 typs_hot"]')

        for block in forBlock:
            ID = block.xpath('div[1]/a[2]/h2/text()')[0] if block.xpath('div[1]/a[2]/h2/text()') else ''
            Text = block.xpath('a[1]/div/span/text()')[0]
            Up = block.xpath('div[2]/span[1]/i/text()')[0]
            Comment  = block.xpath('div[2]/span[2]/a/i/text()')[0]
            print(ID,Text,Up,Comment)
        #for id,text,up,comment in zip(ID,Text,Up,Comment):
            #print(id, '\n', text, '\n', up, '\n', comment, '\n')
#            yield {
#                "id": id,
#                "text": text,
#                "up": up,
#                "comment": comment
#                }
            #return list(id,text,up,comment)
            #print(id,'\n',text,'\n',up,'\n',comment,'\n')
    else:
        pass


def dumpToFile(text):
    pass


if __name__ == "__main__":
    Input = 3 #int(input('Please Input Pages -----'))
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, Input)]
    for url in urls:
        text = getInfo(url)



