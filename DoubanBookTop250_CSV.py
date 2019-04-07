#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 15:48
# @Author  : Peng Y.
# @Site    : 
# @File    : DoubanBookTop250_CSV.py
# @Software: PyCharm


from lxml import etree
import requests
import csv

fp = open('DoubanBookTop250.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}

for url in urls:
    html = requests.get(url,headers = headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0] #'td/p/@class'.没有text（），返回对象
        author = book_infos.split('/')[0]
        publiser = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td[2]/div[2]/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else "空"
        writer.writerow((name,url,author,publiser,date,price,rate,comment))

fp.close()


