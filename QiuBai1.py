# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:13:11 2018

@author: pengyy
"""

import requests
import re
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}


def getInfo(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:

        pattern = '''<div class="article block untagged mb15 typs.*?" id='qiushi_tag_(.*?)'>.*?<h2>(.*?)</h2>.*?<div class="articleGender (.*?)".*?<div class="content">.*?<span>(.*?)</span>'''
        texts = re.findall(pattern, res.text, re.S)  # 使用re.findall方法一次性查找所需内容。
        for i in texts:
            for j in i:
                print(j)

        patternContents = '<div class="content">.*?<span>(.*?)</span>'
        textsContents = re.findall(patternContents, res.text, re.S)  # 使用re.findall方法查找所分四次需内容。
        # for i in textsContents:
        # print(i.strip('\n'))
        patternAuthor = '<h2>(.*?)</h2>'
        textsAuthor = re.findall(patternAuthor, res.text, re.S)
        # for i in textsAuthor:
        # print(i.strip('\n'))
        patternGender = '<div class="articleGender (.*?)"'
        textsGender = re.findall(patternGender, res.text, re.S)
        # for i in textsGender:
        # print(i.strip('\n'))
        patternID = '''<div class="article block untagged mb15 typs.*?" id='qiushi_tag_(.*?)'>'''
        textsID = re.findall(patternID, res.text, re.S)
        # for i in textsID:
        # print(i.strip('\n'))

    else:
        pass


def dumpToFile(texts):
    pass
    # with open('QiuBaiText.txt') as f:
    # pass


if __name__ == "__main__":
    Input = 2  # input('Please Input Pages:  ')
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(int(Input))]
    for url in urls:
        texts = getInfo(url)
        dumpToFile(texts)

'''
①range函数，注意不能输入1，输入1，开始就是0。
②使用re.findall()方法时，pattern提取一个内容时，保存为list，提取多个内容是保存为tuple。
'''