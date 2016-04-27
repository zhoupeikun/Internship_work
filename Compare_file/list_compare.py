import os
import os.path
import fnmatch

def returnold(folder):
    matches = []
    name_complet = []
    name_list = []
    for root, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            matches.append(os.path.join(root, filename))  
    # complet root and name sorted     
    sorted_matches =  sorted(matches, key=os.path.getmtime)
    # complet file name including type
    for name in sorted_matches:
        name_complet.append(name.split("/")[-1])
    # file name not inlcuding type but times
    for names in name_complet:
        name_list.append(names.split(".")[0])
    return name_complet

sent_name = returnold('C:/Users/pzhou/Desktop/test/sent/')
#print sent_name

def walk_dir_received(dir, topdown=True):
    ok_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            #print '.acq' type files
            if name.find('.acq') != -1:
                currentPath = os.path.join(root, name)
                filesize = os.path.getsize(currentPath)
                if filesize == 13:
                    ok_list.append(os.path.join(name))
                else :
                    not_list.append(os.path.join(name))
    return ok_list

dir_received = r'C:/Users/pzhou/Desktop/test/received'
received_name =  walk_dir_received(dir_received)
#print received_name

def compare_list(sent_name, received_name):
    result = []
    sent_list = sent_name
    received_list = received_name
    for sent_name in sent_list:
        for received_name in received_list:
            if sent_name[:40] == received_name[:40]:
                sent_list.remove(sent_name)
                received_list.remove(received_name)
                result.append(sent_name + '\t'+'received')  
                break  
            # else:
            #     result.append(sent_name + '\t'+'not received')
            #     break

    return (result, sent_list)

(result_ok, result_not) = compare_list(sent_name, received_name)
print result_ok
print result_not

file_result = open("list_result.xls", 'w')
for e1 in result_ok:
    file_result.write(e1 + '\n')
for e2 in result_not:
    file_result.write(e2 + '\t' +'not received\n')

# result1 = []
# for e1 in sent_name:
#         for e2 in received_name:
#             if e1[:40] == e2[:40]:
#                 sent_name.remove(e1)
#                 received_name.remove(e2)
#                 result1.append(e1 + '   received') 
#                 break   
#             else:
#                 result1.append(e1 + 'not received')
# print result