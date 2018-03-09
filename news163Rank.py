#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 14:30
# @Author  : Peng Y.
# @Site    : 
# @File    : news163Rank.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}


def getList(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        pattern = '<tr>.*?<td class="rank"><a href="(.*?)">(.*?)</a></td>.*?<td class="cBlue">(.*?)</td>.*?</tr>'
        texts = re.findall(pattern, res.text, re.S)
        for i in texts:
            #print(i[0], '\n', i[1],  '\n', i[2], '\n')
            #print(type(i[0]))
            print(i[0],'\n',i[1],'\n',getInfo(i[0]),'\n',i[2],'\n')
    else:
        pass


#        soup = BeautifulSoup(res.text,'lxml')
#        titles = soup.select('td.red > a')+soup.select('td.rank > a')
#        print(len(titles))
#
#        marks = soup.select('tr > td.cBlue')
#        print(len(marks))
#
#        for i,j in zip(titles,marks):
#            print(i,'\n',j,'\n')
        #body > div.area.areabg1 > div.area-half.left > div > div.tabContents.active > table > tbody > tr:nth-child(2) > td.red > a
        #body > div.area.areabg1 > div.area-half.left > div > div.tabContents.active > table > tbody > tr:nth-child(13) > td.rank > a
        #body > div.area.areabg1 > div.area-half.left > div > div.tabContents.active > table > tbody > tr:nth-child(79) > td.rank
        #body > div.area.areabg1 > div.area-half.left > div > div.tabContents.active > table > tbody > tr:nth-child(3) > td.cBlue

def getInfo(url):
    res = requests.get(url,headers = headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'lxml')
        texts = soup.select('#endText > p')     #不能提取文本

        ##endText > p:nth-child(3)

        return texts
    else:
        pass





if __name__ == "__main__":
    url = 'http://news.163.com/special/0001386F/rank_whole.html'
    getList(url)

'''
①re的pattern参数中碰到换行，加上一个.*?。
'''