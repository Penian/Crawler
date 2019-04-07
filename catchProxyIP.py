#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/25 11:50
# @Author  : Peng Y.
# @Site    : 
# @File    : crawlingWithProxies.py
# @Software: PyCharm

#import requests  # 导入requests模块用于访问测试自己的ip
#import random
#
#pro = ['110.72.26.65:8123']#,'58.45.253.152:61202','119.5.1.16:808','122.114.31.177:808','61.135.217.7:80','119.28.112.130:3128','183.163.45.124:51225','61.144.105.242:9797','14.118.253.158:6666','222.186.45.122:62222','122.237.31.211:61234','124.91.186.203:8118','171.35.14.207:61202','121.237.137.203:3128','115.201.137.54:61202','113.121.246.109:61234','112.245.253.133:61234','175.11.212.141:61234','42.85.165.58:61202','180.122.129.47:61202','183.184.66.142:61202','222.185.160.196:6666','116.248.169.27:80','144.255.122.52:6666','175.171.190.33:53281','111.155.116.216:8123','123.161.237.243:26897','122.235.97.93:8118','115.46.77.245:8123','182.86.191.74:18118','125.118.79.237:808','27.46.51.133:9000','115.46.70.189:8123','218.93.187.38:6666','113.105.203.27:3128','183.54.30.194:9797','222.182.53.254:8118','49.85.1.186:42411','125.120.10.232:6666','60.23.46.47:8118','121.231.144.247:6666','115.204.27.234:6666','39.82.250.113:8118','175.155.24.57:808','58.216.202.149:8118','171.217.59.3:8888','125.121.113.122:808','202.108.2.42:80','221.229.18.7:808','110.73.49.214:8123','116.225.71.29:8118','113.99.218.220:9797','125.104.237.133:22914','114.226.105.145:6666','182.202.220.50:61234','182.202.221.128:61234','117.63.1.213:6666','114.230.41.86:808','59.38.241.36:61234','182.120.12.143:8118','110.73.2.166:8123','111.155.116.237:8123','111.155.124.84:8123','110.73.40.159:8123','110.72.47.71:8123','110.73.53.206:8123','111.155.116.245:8123','222.186.45.121:52163','49.83.30.25:8888','175.148.73.177:1133','14.118.253.81:6666','111.155.116.242:8123','60.184.172.103:808','114.230.41.33:3128','49.79.194.201:61234','61.147.118.26:35270','49.79.194.158:61234','125.120.205.12:6666','144.255.123.155:61234','110.73.12.108:8123','14.118.253.104:6666','183.20.8.134:61234','119.5.1.17:808','222.185.3.72:6666','222.220.156.106:61202','114.113.126.86:80','49.79.195.142:61234','180.118.242.249:61234','222.186.45.59:62386','125.118.245.18:6666','222.186.45.135:53281','182.88.134.182:8123','115.192.86.224:8118','114.228.155.127:1133','115.221.117.136:48857','125.121.122.132:808','125.118.242.194:6666','112.67.173.135:9797','111.155.116.225:8123','110.83.174.156:25020']
## 在(http://www.xicidaili.com/wt/)上面收集的ip用于测试
## 没有使用字典的原因是 因为字典中的键是唯一的 http 和https 只能存在一个 所以不建议使用字典
#
#
#head = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#url = 'http://www.whatismyip.com.tw/'  # 你用于测试自己ip的网站
#request = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)
# # 让问这个网页  随机生成一个ip
#request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
#print(request.text)  # 输出返回的内容




import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def catchProxyIP(page):
    timestamp = time.strftime('%Y-%m-%d %X', time.localtime())
    title = "[" + timestamp + "]" + "Begin to Crawl Page" + str(page) + "of Proxies. "
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    #print("page:", page)

    url = 'http://www.xicidaili.com/nn/' + str(page)
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    #print(soup)
    ips = soup.find_all('tr')
    for x in range(1,len(ips)):
        ip = ips[x]
        tds = ip.find_all('td')
        ipTemp = tds[1].contents[0]+"\t"+tds[2].contents[0]+'\n'
        if (checkProxyAvaliable(tds[1].contents[0],tds[2].contents[0])):
            with open('catchProxyIP.txt', 'a+') as f:
                f.write(ipTemp)
        print (ipTemp)

def checkProxyAvaliable(ip,port):
    timestamp = time.strftime('%Y-%m-%d %X',time.localtime())
    title = '['+timestamp+']'+'Begin to parse the IP to identify if it is valid. '
    print('\n',title)
    proxyHost = 'http://'+ip+':'+port
    proxyTemp = {'http':proxyHost}
    url = "http://ip.chinaz.com/getip.aspx"
    try:
        res = requests.get(url,proxies = proxyTemp)
        print(proxyTemp)
        print(res.text,'Proxy is OK')
        return True
    except Exception as e:
        print(e)


if __name__ == "__main__":
    pool = Pool(processes = 2)
    pool.map(catchProxyIP,range(1,20))
    #for p in range(1,20):  #one process
    #    catchProxyIP(p)