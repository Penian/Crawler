#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 14:28
# @Author  : Peng Y.
# @Site    :
# @File    : QiuBai_XPath_MySQL.py
# @Software: PyCharm

import requests
from lxml import etree
import pymysql
import time
import random
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

def dumpToMySQL(id,text,up,comment):
    db = pymysql.connect(host='10.128.4.203', user='atmin', password='admin', db='pyCrawler', port=33060,charset='utf8')
    cur = db.cursor()
    cur.execute('insert into QiuBai(id,text,up,comment) values(%s,%s,%s,%s)',(str(id),str(text),int(up),int(comment)))
    db.commit()

def getInfo(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        html = etree.HTML(res.text)
        forBlock = html.xpath('//div[@class="article block untagged mb15 typs_old"]') + html.xpath('//div[@class="article block untagged mb15 typs_hot"]')  #属性值后面不一致
        for block in forBlock:
            ID = block.xpath('div[1]/a[2]/h2/text()')[0] if block.xpath('div[1]/a[2]/h2/text()') else '匿名用户'    #消除空ID影响
            Text = block.xpath('a[1]/div/span/text()')[0]
            Up = block.xpath('div[2]/span[1]/i/text()')[0]
            Comment  = block.xpath('div[2]/span[2]/a/i/text()')[0]
            print(ID,Text,Up,Comment)
            dumpToMySQL(ID, Text, Up,Comment)
    else:
        pass

if __name__ == "__main__":
    Input = int(input('Please Input Pages -----'))
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, Input)]
    db = pymysql.connect(host='10.128.4.203', user='atmin', password='admin', db='pyCrawler', port=33060,charset='utf8')

    cur = db.cursor()
    cur.execute('drop table if exists QiuBaiMultiProcess')
    cur.execute('create table QiuBaiMultiProcess (id varchar(20),text text(1024),up int,comment int)') #使用text类型，str只能到255。
    db.close()
    #for url in urls:
    #    text = getInfo(url)


    with Pool(1) as p:
        p.map(getInfo,urls)


    db.close()

    #time.sleep(random.random())




