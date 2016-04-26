s = 'COFREP-B00000390-2015-05-SLCRXX-00-L-N--'
#print len(s)

str1 = 'COFREP-B00000390-2015-05-SLCRXX-00-L-N--'
str2 = 'COFREP-B00000390-2015-05-SLCRXX-00-L-N--'

def compare_name(str1, str2):

	if str1 == str2:
		return 1
	else :
		return 0

compare_name(str1, str2)


dir_sent = r'C:/Users/pzhou/Desktop/test/sent/'
file_sent = open("sent.txt", 'r+')

# for line in file_sent:
# 	print line[:40]





def print_result(sent, received, result):
	sent_length = len(sent.readlines())
	received_length = len(received.readlines())

	for line2 in received:
		for line1 in range(0, 5):
			for line1 in sent:
				if line1[:40] == line2[:40]:
					result.write(line1 + '  OK'  '\n')
					print 1
				else:
					result.write(line1 + '  Not OK' '\n')
					print 0 

def print_list_result(sent, received, result):
	for i, j in zip(sent_list, received_list):
		if i[:40] == j[:40]:
			print 1
			print i
			result.write(i + 'OK' '\n')
		# else:
		# 	print 0
		# 	result.write(i + 'not OK' '\n')

# def print_list_result2(sent, received, result):


file_sent = open("sent.txt", 'r')
file_received = open("received.txt", 'r')

sent_list = file_sent.readlines()
received_list = file_received.readlines()
# length of list
sent_length = len(sent_list)
received_list = len(received_list)

result = open('result.txt', 'w')

print_result(file_sent, file_received, result)

# print_list_result(sent_list, received_list, result)

