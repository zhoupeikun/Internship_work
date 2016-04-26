
with open('sent.txt', 'r') as sent_file:
	with open('received.txt', 'r') as received_file:
		notsame = set(sent_file).difference(received_file)


with open('sent.txt', 'r') as sent_file:
	with open('received.txt', 'r') as received_file:
		same = set(sent_file).intersection(received_file)

# same.discard('\n')
print same
print notsame


with open('some_output_file.txt', 'w') as file_out:
	file_out.write('Received OK\n')
	
	for line1 in same:
		file_out.write(line1)

	file_out.write('\nNot received: \n')
	for line2 in notsame:
		file_out.write(line2)

