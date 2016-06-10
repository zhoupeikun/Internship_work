 #!/usr/local/bin/python
 # coding: utf-8

import os
import time
import xlwt

event_file = open('Events.csv', 'r')

# today_time = time.strftime("%d/%m/%Y", time.localtime())
today_time = '27/05/2016'

print today_time
# time format, 06/01/2090  17:33:18
# event format, 27/04/2016  14:53:08;0006;DING Jiang (6);Access allowed;Right Entrance (side 1)

# today_recording store today's events or the select day's events
today_recording = []

for line in event_file:
	if line[:10] == today_time: 
		if line.split(";")[3] == ("Access allowed"):
			today_recording.append(line)
#		print line
# print today_recording[0][21:25]
# print today_recording[0] 

#print today_recording
#print len(today_recording)

name_list = ['ZHUANG Jie(1)', 'WANG Xiaoyou(2)', 'CAO Peng(3)', 'VON KUNOW Moritz(4)', 'XU Chi (5)', 'DING Jiang (6)', 'WANG Yue', 'JIANG Jie', 'CHEN Li (9)', 'WANG Xuemei (10)', 'MANSO Guillaume (11)', 'RAMELLI Jerome', 'Lambot Jean-Marc (14)', 
			'ZHOU Bin (15)', 'OLDING Jennifer-secondcard', 'OLDING Jennifier (19)', 'PADILLA MAYER Helios (16)', 'HEUSEL Michael (17)', 'BURGUN Jean-Yves(18) ', 'ZONG Yuanyuan', 'Intern Receptionist', 'Xu Fei (20)', 'LI Yidai (21)', 'LIU-GERHARDS Yang (22)', 'HENG Ze', 'ZHOU Peikun ', 'RISK Intern']
print len(name_list)

# name_first store the first event of each one
# name_last  store the last event of each one
name_last = {}
name_first = {}
l1=[]
l2=[]
for log in today_recording:
	if name_last.has_key(log.split(";")[2]):
		name_last[log.split(";")[2]] = log.split(";")[0]
	else:
		name_last[log.split(";")[2]] = log.split(";")[0]
		name_first[log.split(";")[2]] = log.split(";")[0]
		
print name_last
print name_first
print len(name_last)
print len(name_first)


result = {}
for name in name_list:
	for (k1, v1) in name_last.items():
		for (k2, v2) in name_first.items():
			if name == k1 and k1 == k2:
				result[k1] = v2[:12] + "\t" + v2[12:] + '\t' + v1[12:]
				#name_list.remove(name)
			else:
				continue
	#result[]

print result
print len(result)

for key in result:
	for name in name_list:
		if key == name:
			name_list.remove(name)
		else:
			continue
print name_list
	


result_file = open("result.xls", 'w')
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('sheet')


for key in result:
	if int(result[key][13:15]) > 8 :
		if int(result[key][22:24]) < 17 :
			result_file.write(key + '\t' + result[key] + '\t Arrived later and left early' + '\n')
			#worksheet.write()
		else :
			result_file.write(key + '\t' + result[key] + '\t Arrived later' + '\n')
	elif int(result[key][22:24]) < 17 :
		result_file.write(key + '\t' + result[key] + '\t Left early' + '\n')
	else: 
		result_file.write(key + '\t' + result[key] + '\n')

for name in name_list:
	result_file.write(name + '\t Absence' + '\n')