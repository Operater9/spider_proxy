#!/usr/bin/env python
# coding=utf-8
"""
    脚本功能：
        获取代理IP（国内高匿代理）,使用代理IP是爬虫脚本功能中的一部分

    环境要求：
        1：python版本 3.6.1；
        2：安装bs4库: pip install beautifulsoup4
        3：安装requests库：pip install requests
"""

import re
from random import choice
import requests
import bs4

url = "http://www.xicidaili.com/nn"
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.xicidaili.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

r = requests.get(url,headers=headers)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
data = soup.table.find_all("td")

ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
port_compile = re.compile(r'<td>(\d+)</td>')
ip = re.findall(ip_compile,str(data))
port = re.findall(port_compile,str(data))

ips = [":".join(i) for i in zip(ip,port)]
# print("代理IP列表：{ip_list}".format(ip_list=ips))
print("随机在代理IP列表中选一个IP：{ip}".format(ip=choice(ips)))
