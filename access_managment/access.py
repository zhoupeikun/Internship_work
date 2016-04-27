import os
import time

event_file = open('C:/Users/pzhou/Desktop/events_0427.csv', 'r')

today_time = time.strftime("%d/%m/%Y", time.localtime())
print today_time
# time format, 06/01/2090  17:33:18
# event format, 27/04/2016  14:53:08;0006;DING Jiang (6);Access allowed;Right Entrance (side 1)

today_recording = []

for line in event_file:
	if line[:10] == today_time and line.find('Access'):
		today_recording.append(line)
#		print line
print today_recording[0]

for log in today_recording:
	



