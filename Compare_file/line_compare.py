
def line_compare(sent, received, result):
	for line1 in sent:
		#str1 = line1[:40]
		#print str1
		print line1
		for line2 in received:
			str2 = line2[:40]
			#print str1
			print line2



file_sent = open("sent.txt", 'r')
file_received = open("received.txt", 'r')
result = open('result.txt', 'w')

line_compare(file_sent, file_received, result)

file_sent.close()
file_received.close()
result.close()