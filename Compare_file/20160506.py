import os
import os.path
import fnmatch

# BCL_Statistics and FINREP files in Conceptlance(224.4) and Efile(224.146)
# 224.4 is the server where file generated
# 224.146 is the server where file to be sent and receipt records

# Function record file genrenated to be sent
# Server: 224.4 Conceptlance
# 
def walk_dir_sent(folder):
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

# Record BCL_Statistics file generated
bcl_sent_name = walk_dir_sent('XXXXXX:/BCL_Statistics/')

#Record FINREP file generated
finrep_sent_name = walk_dir_sent('XXXXXX:/FINREP/')


# Function record file have been received
# Server: 224.146 Efile
# Efile - BCL_Statistics
#       - FINREP
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

# BCL_Statistics and FINREP ACQ file folders
dir_bcl = r'I:/BCL_Statistics/'
dir_finrep = r'I:/FINREP/'

# record BCL_Statistics files received
bcl_received_name =  walk_dir_received(dir_bcl)
# record FINREP files received
finrep_received_name = walk_dir_received(dir_finrep)
#print received_name



# Functiomn Compare to return results
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

# BCL_Statistics result to list_bcl_result.xls
(result_bcl_ok, result_bcl_not) = compare_list(bcl_sent_name, bcl_received_name)
print result_bcl_ok
print result_bcl_not

# If select incremental write, 'w' -> 'a'
file_bcl_result = open("list_bcl_result.xls", 'w')
for e1 in result_bcl_ok:
    file_bcl_result.write(e1 + '\n')
for e2 in result_bcl_not:
    file_bcl_result.write(e2 + '\t' +'not received\n')

# FINREP result to list_finrep_result.xls
(result_finrep_ok, result_finrep_not) = compare_list(finrep_sent_name, finrep_received_name)
print result_finrep_ok
print result_finrep_not

file_finrep_result = open("list_finrep_result.xls", 'w')
for e3 in result_finrep_ok:
    file_finrep_result.write(e3 + '\n')
for e4 in result_finrep_not:
    file_finrep_result.write(e4 + '\t' +'not received\n')


# TO DO
# Function movefile to move the sent files who have recepted acq-OK
# 


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