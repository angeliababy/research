# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:03:06 2017

@author: Administrator
"""
#批量检查url有效性
import urllib2
from urllib2 import URLError
import xlwt
import datetime,time
import requests
from lxml import etree

result_url=[]
result = []
count=0
not_200=0
f=open("app0306.txt","r")    # 域名或网址的txt文件

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My workshet')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
headers = { 'User-Agent' : user_agent }
for line in f:
    count+=1
    print "on scanning ",count
    try:
        # req = requests.request("get", "http://" + line)
        # print req.status_code

        req = urllib2.Request(line, headers = headers)   # 网址
        #req = urllib2.Request("http://" + line) #域名
        response = urllib2.urlopen(req)
        data = response.read()
        data = data.decode('utf-8')
    except URLError, e:
        if hasattr(e,'reason'): #stands for URLError
            print "can not reach a server,writing..."
        elif hasattr(e,'code'): #stands for HTTPError
            print "find http error, writing..."
        else: #stands for unknown error
            print "unknown error, writing..."
        not_200 += 1
        # result_url.append(line)
        # result.append('NO')
        re = 'NO'
        time.sleep(1)  # 休眠1秒
    else:
        #print "url is reachable!"
        #else 中不用再判断 response.code 是否等于200,若没有抛出异常，肯定返回200,直接关闭即可
        #result.append('YES')
        print "Yes!"
        response.close()
        time.sleep(1)  # 休眠1秒
        re = 'YES'
    finally:
        pass

    if re == 'YES':
        selector = etree.HTML(data)
        content1 = selector.xpath('//div[@class="details-info"]/div/div/h1/div/text()')
        # for i in content1:
        #     print i
        content2 = selector.xpath('//div[@class="left-info"]/div/a/span[@itemprop="genre"]/text()')
        # for j in content2:
        #     print j
        worksheet.write(count-1, 0, line)  # 1列
        worksheet.write(count-1, 1, content1)  # 2列
        worksheet.write(count-1, 2, content2)  # 2列
    else:
        worksheet.write(count-1, 0, line)  # 1列
        worksheet.write(count-1, 1, "NO")  # 2列

    # worksheet.write(count-1, 0, line)  # 1列
    # worksheet.write(count-1, 1, re)  # 2列
    workbook.save('appmonth.xls')

print "scanning over,total",count,"; did not response 200:",not_200
f.close()
