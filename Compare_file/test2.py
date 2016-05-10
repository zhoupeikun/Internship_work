import os

# def listDir(rootDir):
#     for filename in os.listdir(rootDir):
#         pathname = os.path.join(rootDir, filename)
#         if (os.path.isfile(filename)):
#             print pathname
#         else:
#             listDir(pathname)

# listDir('I:\DOC_BNK')




# print os.path.isfile('J:\Plexus Export File\BCL_Statistics\S0001_L1_20160506_B000000390_B000000390_20160509_001.xml')




for filename in os.listdir('J:\Plexus Export File\BCL_Statistics'):
	if (os.path.isfile('J:/Plexus Export File/BCL_Statistics/' + filename)):
		print filename
   	else:
   		print 'No'

def walk_dir_sent(folder):
    matches = []
    name_complet = []
    name_list = []
    sorted_matches = []
    #for filenames in os.listdir(folder):
    for filename in os.listdir(folder):
        if(os.path.isfile(folder+filename)):
            matches.append(os.path.join(folder, filename))  
    # complet root and name sorted by modified time
    sorted_matches =  sorted(matches, key=os.path.getmtime)
    for name in sorted_matches:
        name_complet.append(name.split("/")[-1])
    print name_complet

bcl_sent_name = walk_dir_sent('J:/Plexus Export File/BCL_Statistics/')


for e1 in [1,2,3,4,5,6]:
	if e1 in [2,3,4]:
		continue
	else:
		print e1