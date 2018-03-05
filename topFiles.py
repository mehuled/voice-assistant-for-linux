#from __future__ import division
import os, shutil, sys
import webbrowser
import time
from time import strftime


#---------------- Function to return the size in appropriate units i.e Bytes, KB or MB.----------------

def getsize(bytes) :                            
	if bytes < 1024 :
		return "%s %s" % (str(bytes),"Bytes")

	elif bytes>=1024 and bytes <1024*1024 :
		return "%s %s" % (str(bytes//1024),"KB")

	else :
		return "%s %s" % (str(bytes//(1024*1024)),"MB")


#------------------ To deal with command line arguments provided---------------------------------

reverse = True
lookAll = False 

if len(sys.argv) == 1 :
	count = 10	#Default : Show ten entries.			
	sortby = 1   #Default : Sort by size only
	 

elif len(sys.argv) == 2 :
	
	
	if sys.argv[1] == 'lat' :
		
		sortby = 2
		count = 10 
		
	elif sys.argv[1] == 'eat' :
		
		sortby = 2
		count = 10 
		reverse = False
		
	elif sys.argv[1] == 'all' :


		sortby = 1
		count = 10 
		lookAll = True


	else :
		try :
			count = int(sys.argv[1])
			sortby = 1 
		except :
			print ("Invalid Argument")
			sys.exit(1)

elif len(sys.argv) == 3 :

	try :
		count = int(sys.argv[1])
		
		if sys.argv[2] == 'lat' :
			
			sortby = 2 
		elif sys.argv[2] == 'eat' :
		
			sortby = 2 
			reverse = False
		
		else :
			print ("Invalid argument for sort by parameter. Sorting by size only!")
			sortby = 1 
		
		
	except :
		print ("Invalid Argument for number of files to be shown. Exiting!")
		sys.exit(1)
 


else :
	print ("Too many arguments provided. Running in default mode!")
	count = 10 
	sortby = 1 


#-------------------- Code to recursively access all the files in listed directories and append their info in a list ----------------


if sortby == 1 :
	time_format = "%b %d, %Y" 	#when sorting by size only date of last access is needed

else :
	time_format = "%H:%M | %b %d, %Y" 	#when sorting by last access time, Hour minute and date are shown



directory = os.environ["HOME"]


if lookAll :
	
	directoriesToBeChecked = [""]

else :
	directoriesToBeChecked = ['/Desktop','/Documents','/Downloads','/Music','/Pictures','/Movies','/Videos']

fileinfo = []

for destinationFolder in directoriesToBeChecked :


	for root, directories, filenames in os.walk("%s%s" %(directory,destinationFolder)) :
		for filename in filenames :
	
			try :
				fileinfo.append((os.path.join(root,filename),os.stat(os.path.join(root,filename)).st_size,os.stat(os.path.join(root,filename)).st_atime,strftime(time_format, time.localtime(os.stat(os.path.join(root,filename)).st_atime))))

				#print os.path.join(root,filename)
		
		
		
			except OSError :
		
				print ("Found file which is non existent, so moving on!")
		
		
		

#---------------- To sort the file info on a parameter, defaults to size or last access time if lat is provided as command line argument

fileinfo.sort(key=lambda x : x[sortby],reverse=reverse)

html_body = ''


for i in range(count) :
	html_body =  "%s <tr> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> </tr>" %(html_body,(i+1),fileinfo[i][0],getsize(fileinfo[i][1]),fileinfo[i][3])  	




#------------ Code to generate the webpage of a table listing the top 10 files by size----------------



html_start = '''<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>

<table>
 <colgroup>
       <col span="1" style="width: 5%;">
       <col span="1" style="width: 50%;">
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 25%;">
       
    </colgroup>
  <tr>
    <th>S. No</th>
    <th>Filename</th>
    <th>Size</th>
    <th>Last accessed</th>
  </tr>'''
  
  
  
html_end = '''</table>

</body>
</html>
'''


Html_file= open("%s%s%s" % (os.environ['HOME'],"/Desktop","/topfiles.html"),"w")
Html_file.write("%s %s %s" % (html_start,html_body,html_end))
Html_file.close()

#This is used to automatically open the html file in browser



webbrowser.open("%s%s%s" % (os.environ['HOME'],"/Desktop","/topfiles.html")) 
print ("Success")








	
