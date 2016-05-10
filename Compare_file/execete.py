import os
import time




tmp_bcl_ok = []
tmp_bcl_not = []
tmp_finrep_ok = []
tmp_finrep_not = []

for i in range (1000):
	print i
	execfile('20160506.py')
	execfile('tmp_write.py')
	time.sleep(120)