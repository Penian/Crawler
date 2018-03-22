#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 8:20
# @Author  : Peng Y.
# @Site    : 
# @File    : DoubanMusicTop250.py
# @Software: PyCharm

import pymongo
import requests
from lxml import etree
import time
import datetime
import re


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

client = pymongo.MongoClient('mongodb://root:Toor1@10.128.4.203:27017')
myDb = client['myDb']
musicTop250 = myDb['musicTop250']
musicTop250.insert_one({'name':'test','time':datetime.datetime.now()})

def getUrl(url):
    resUrl = requests.get(url,headers = headers)
    htmlUrl = etree.HTML(resUrl.text)
    #print(resUrl.text)
    # sgUrl = htmlUrl.xpath('//div/div/div/div[1]/div/table[1]/tbody/tr/td[2]/div/a/@href')
    sgUrl = htmlUrl.xpath('//a[@class="nbg"]/@href')
    # sgUrl = htmlUrl.xpath('//a/@href')
    for i in sgUrl:
        getInfo(i)


def getInfo(url):
    res = requests.get(url,headers = headers)
    #print(res.text)
    html = etree.HTML(res.text)

    name = html.xpath('//*[@id="wrapper"]/h1/span/text()')
    print(name)
    #aliasName = html.xpath('//*[@id="info"]/text()[1]')

    singer = re.findall('表演者:.*?">(.*?)</a>',res.text,re.S)
    style = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />', res.text, re.S)

    ImEx = re.findall('<span class="pl">专辑类型:</span>&nbsp;(.*?)<br />',res.text,re.S)

    MediaType = re.findall('<span class="pl">介质:</span>&nbsp;(.*?)<br />',res.text,re.S)
    PubTime = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />',res.text,re.S)

    Publisher = re.findall('<span class="pl">出版者:</span>&nbsp;(.*?)<br />',res.text,re.S)

    BarCode = re.findall('<span class="pl">条形码:</span>&nbsp;(.*?)<br />',res.text,re.S)

    ISRC = re.findall('<span class="pl">ISRC.*?:</span>&nbsp;(.*?)<br />',res.text,re.S)

    musicTop250.insert_one({'songName':name[0],
                            'singer':singer[0] if len(singer)!=0 else '',
                            'style':style[0] if len(style)!=0 else '',
                            'ImEx':ImEx[0] if len(ImEx)!=0 else '',
                            'MediaType':MediaType[0] if len(MediaType)!=0 else '',
                            'PubTime':PubTime[0] if len(PubTime)!=0 else '',
                            'Publisher':Publisher[0] if len(Publisher)!=0 else '',
                            'BarCode':BarCode[0] if len(BarCode)!=0 else '',
                            'ISRC':ISRC[0] if len(ISRC)!=0  else ''})



if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    #print(urls)
    for url in urls:
        getUrl(url)
    #url = 'https://music.douban.com/top250?start=0'
    #getUrl(url)



