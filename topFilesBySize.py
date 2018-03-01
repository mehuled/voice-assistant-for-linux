#from __future__ import division
import os, shutil

directory = os.environ["HOME"]

directoriesToBeChecked = ['/Desktop','/Documents','/Downloads','/Music','/Pictures','/Videos']

fileinfo = []

for destinationFolder in directoriesToBeChecked :


	for root, directories, filenames in os.walk("%s%s" %(directory,destinationFolder)) :
		for filename in filenames :
	
			try :
				fileinfo.append((os.path.join(root,filename),os.stat(os.path.join(root,filename)).st_size/(1024*1024)))
		
			except OSError :
		
				print ""
		
			#print os.path.join(root,filename)
		
			#print os.stat(os.path.join(root,filename)).st_size
		
fileinfo.sort(key=lambda x : x[1],reverse=True)

for i in xrange(10) :
	print "%s | %s MB" %(fileinfo[i][0],fileinfo[i][1])  	
	
