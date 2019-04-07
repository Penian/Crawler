#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 13:02
# @Author  : Peng Y.
# @Site    : 
# @File    : urlCrawler.py
# @Software: PyCharm

import requests
import re
import random

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
proxies = ['14.118.254.97:6666','58.19.80.248:18118','171.39.1.81:8123']
urlList = []

def resUrl(url):
    try:
        res = requests.get(str(url), headers=headers)#, proxies={'http':random.choice(proxies)})
        res.encoding = res.apparent_encoding
        if res.status_code == 200 :
            return res
        else:
            pass
    except  (requests.exceptions.SSLError,requests.exceptions.ConnectionError,requests.exceptions.TooManyRedirects) as e:
        pass

def findUrl(res):
    if res:
        find = re.findall('href="(https?://.*?)"', res.text)
        return find
    else:
        return []

def dumpToList(url):
    global urlList
    res = resUrl(url)
    urlList += findUrl(res)
    return urlList

def writeToFile(urlList):
    with open('urlCrawler.txt', 'a+') as f:
        for i in urlList:
            try:
                f.write(str(i) + '\n')
            except UnicodeEncodeError as e:
                pass

if __name__ == "__main__":
    urlInput = []
    urlStart = input('Please Enter the starting URL____')  #'http://www.189.cn'
    urlInput.append(urlStart)
    depth = int(input('Please Enter the depth (1~2) ____'))    #10^2
    while depth > 0 :
        print(urlInput)
        for i in urlInput:
            dumpToList(i)
        urlInput = list(set(urlList))   #list(set())
        depth -= 1
    writeToFile(list(set(urlList)))     #90K > 6K


