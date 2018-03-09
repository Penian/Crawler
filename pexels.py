#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 15:43
# @Author  : Peng Y.
# @Site    : 
# @File    : pexels.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
import json

headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

word = input('Please Input The Picturs\' Name ----')
url = 'https://www.pexels.com/search/' + word

#url_tra = 'http://howtospeak.org:443/api/e2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text=' + word

res = requests.get(url,headers = headers)
soup = BeautifulSoup(res.text,'lxml')
#print(soup)
imgs = soup.select('article > a > img')
list = []
for img in imgs:
    photo = img.get('src')
    list.append(photo)

path = 'pexels/'

for i in list:
    data = requests.get(i,headers = headers)
    with open(path + word+'_'+i.split('?')[0][-10:],'wb') as f:
        f.write(data.content)

'''
①soup.select参数中selector，尖括号两端有空格。
'''