import os
import time

event_file = open('test.csv', 'r')

# today_time = time.strftime("%d/%m/%Y", time.localtime())
today_time = '27/04/2016'

print today_time
# time format, 06/01/2090  17:33:18
# event format, 27/04/2016  14:53:08;0006;DING Jiang (6);Access allowed;Right Entrance (side 1)

today_recording = []

for line in event_file:
	if line[:10] == today_time: 
		if line.split(";")[3] == ("Access allowed"):
			today_recording.append(line)
#		print line
# print today_recording[0][21:25]

#print today_recording[0] 

#print today_recording
print len(today_recording)

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
for (k1, v1) in name_last.items():
	for (k2, v2) in name_first.items():
		if k1 == k2:
			result[k1] = v2 + "\t" + v1[12:]
		else:
			continue
print result

result_file = open("result.xls", 'w')


for key in result:
	if int(result[key][12:14]) > 8 :
		if int(result[key][21:23]) < 17 :
			result_file.write(key + '\t' + result[key] + '\tArrived Later and Left Later' + '\n')
		else :
			result_file.write(key + '\t' + result[key] + '\tArrived Later' + '\n')
	elif int(result[key][21:23]) < 17 :
		result_file.write(key + '\t' + result[key] + '\tLeft early' + '\n')
	else: 
		result_file.write(key + '\t' + result[key] + '\n')