# 27/04/2016  15:37:52;0003;CAO Peng(3);Access allowed;Right Entrance (side 1)
# encoding: utf-8

l ='27/04/2016  15:37:52;0003;CAO Peng(3);Access allowed;Right Entrance (side 1)'

print l.find('15:37:52')
print l[0]

print l [12:-1]
print l[21:25]

s = '27/04/2016  17:17:33'

print s[12:]

s1 = '27/04/2016  07:09:14\t21:52:11'
print s1[12:14]

print s1[21:23]

import xlwt
import xlrd




workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建表
worksheet = workbook.add_sheet('My Worksheet')
# 往单元格内写入内容
worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
# 保存
workbook.save('Excel_Workbook.xls')