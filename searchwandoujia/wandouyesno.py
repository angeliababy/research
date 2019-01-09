# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:03:06 2017

@author: Administrator
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xlrd
import xlwt
import urllib2

data = xlrd.open_workbook('app1201.xlsx')
table = data.sheets()[0]

n_row = table.nrows
n_col = table.ncols

x = []
y = []
for i in range(n_row):
    x.append(table.row_values(i)[0])

count=0
for xx in x:
    url = xx
    # 发起请求
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)

    data = fd.read()
    data = data.decode('utf-8')
    # print(type(data))
    count += 1
    print "on scanning ", count
    if '抱歉，豌豆们没有找到这个页面...' in data:
        y.append('N0')
        print('NO')
    else:
        y.append('Yes')
        print('Yes')

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My workshet')

for i in range(len(x)):
    zz = "http://www.wandoujia.com/apps/"  #删除网址前缀
    l = len(zz)
    add_x = x[i][l:]
    # worksheet.write(i,0,x[i])
    worksheet.write(i, 0, add_x)  # 1列
    worksheet.write(i, 1, y[i])  # 2列

workbook.save('app.xls')










