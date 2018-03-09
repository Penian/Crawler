#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:50
# @Author  : Peng Y.
# @Site    : 
# @File    : MaoYanDianYinTop100.py
# @Software: PyCharm

import requests
import re
from requests.exceptions import RequestException
import time
import json


def get_one_page(Url):
    headers = {
        "Referer": "http://maoyan.com/board",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
    }
    try:
        resp = requests.get(Url, headers=headers)
        if resp.status_code == 200:
            return resp.text
    except RequestException as e:
        raise e


def parse_one_page(html):
    # pattern = re.compile('<dd>.*?board-index-1.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',re.S)
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": item[2],
            "star": item[3].strip()[3:],
            "time": item[4].strip()[5:],
            "score": item[5] + item[6]
        }


def write_to_file(content):
    with open("MYDX100.txt", "a", encoding='utf-8') as f:  #
        f.write(json.dumps(content, ensure_ascii=False) + "\n")
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        # print(item)
        write_to_file(item)


if __name__ == '__main__':
    print("*" * 20 + time.strftime("%Y-%m-%d %H:%M:%S") + "*" * 20)
    for i in range(10):
        main(i * 10)