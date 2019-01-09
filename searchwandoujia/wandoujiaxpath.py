# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xlrd
import xlwt
import urllib2
from lxml import etree

data = xlrd.open_workbook('app0306.xlsx')
table = data.sheets()[0]
n_row = table.nrows
n_col = table.ncols

x = []
y = []
for i in range(n_row):
    x.append(table.row_values(i)[0])

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('app')
count = 0
for xx in x:
    url = xx
    # 发起请求
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)

    data = fd.read()
    data = data.decode('utf-8')
    # print(type(data))

    print "on scanning ", count + 1
    if '抱歉，该应用已下架' in data:
        y.append('N0')
        flag = 'NO'
        print('NO')
    else:
        y.append('Yes')
        flag = 'Yes'
        print('Yes')

    selector = etree.HTML(data)
    zz = "http://www.wandoujia.com/apps/"  # 删除网址前缀
    l = len(zz)
    if flag == 'Yes':
        content1 = selector.xpath('//div[@class="app-info"]/p/span/text()')
        # for i in content1:
        #     print i
        content2 = selector.xpath('//div[@class="col-right"]/div/dl/dd/a/text()')
        # for j in content2:
        #     print j
        worksheet.write(count, 0, url[l:])  # 1列
        worksheet.write(count, 1, content1)  # 2列
        worksheet.write(count, 2, content2)  # 2列
    else:
        worksheet.write(count, 0, url[l:])  # 1列
        worksheet.write(count, 1, "NO")  # 2列
    count += 1
    workbook.save('app.xls')

