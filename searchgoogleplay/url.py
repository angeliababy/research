# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-

import xlwt
import requests

f=open("domain.txt","r")    #域名的txt文件
#img_not_200=open("img_not_200.txt","w+")

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My workshet')

# url1="http://www.fgjdkfgldfg.com"
# url2="http://www.baidu.com"
# url3="http://aipboss.m.tb.cn/ "

# count=0
# not_200=0
# for line in f:
#     count+=1
#     print "on scanning ",count
#     print  "http://" + line.strip()
#     try:
#         r = requests.post("http://"+line.strip())
#         re = 'YES'
#         not_200+=1
#         print True
#     except:
#         re = 'NO'
#         print False
#     worksheet.write(count - 1, 0, line)  # 1列
#     worksheet.write(count - 1, 1, re)  # 2列
#     workbook.save('C:/Users/chenzhuo/Desktop/appweek.xls')
#
# print "scanning over,total", count, "; did not response 200:", not_200
# f.close()