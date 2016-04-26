import os
import os.path

#dir: target map folder
#fileinfo: target written file

#valid file name is 40, name[:40]
#for the file sent
def walk_dir_sent(dir, fileinfo, topdown=True):
	for root, dirs, files in os.walk(dir):
		for name in files:
			fileinfo.write(os.path.join(name)+ '\n')

#for the file received
def walk_dir_received(dir, fileinfo, topdown=True):
	for root, dirs, files in os.walk(dir):
		for name in files:
			#print '.acq' type files
			if name.find('.acq') != -1:
				currentPath = os.path.join(root, name)
				filesize = os.path.getsize(currentPath)
				if filesize == 13:
					fileinfo.write(os.path.join(name)+ '\n')
				else :
					fileinfo.write(os.path.join(name)+  '\n')
	
def print_result(sent, received, result):
	for line1 in sent:
		for line2 in received:
			if line1[:40] == line2[:40]:
				result.write(line1 + '  OK'  '\n')
			else:
				result.write(line1 + '  Not OK' '\n')



dir_sent = r'C:/Users/pzhou/Desktop/test/sent/'
dir_received = r'C:/Users/pzhou/Desktop/test/received'

file_sent = open("sent.txt", 'w')
file_received = open("received.txt", 'w')

# file_sent_read = open("sent.txt", 'r')
# file_received_read = open("received", 'r')

walk_dir_sent(dir_sent, file_sent)
walk_dir_received(dir_received, file_received)

# result = open('result.txt', 'w')

# print_result(file_sent, file_received, result)



file_sent.close()
file_received.close()

