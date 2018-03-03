#from __future__ import division
import os, shutil, sys
import webbrowser
import time
from time import strftime


if len(sys.argv) == 1 :
	count = 10
else :
	try :
		count = int(sys.argv[1])
	except :
		print "Invalid Argument"
		sys.exit(1)
 
directory = os.environ["HOME"]

directoriesToBeChecked = ['/Desktop','/Documents','/Downloads','/Music','/Pictures','/Videos']

fileinfo = []

for destinationFolder in directoriesToBeChecked :


	for root, directories, filenames in os.walk("%s%s" %(directory,destinationFolder)) :
		for filename in filenames :
	
			try :
				fileinfo.append((os.path.join(root,filename),os.stat(os.path.join(root,filename)).st_size/(1024*1024),strftime("%b %d, %Y", time.localtime(os.stat(os.path.join(root,filename)).st_atime))))
		
			except OSError :
		
				print "Found file which is non existent, so moving on!"
		
			#print os.path.join(root,filename)
		
			#print os.stat(os.path.join(root,filename)).st_size
		
fileinfo.sort(key=lambda x : x[1],reverse=True)

html_body = ''

for i in xrange(count) :
	html_body =  "%s <tr> <td> %s </td> <td> %s </td> <td> %s MB </td> <td> %s </td> </tr>" %(html_body,(i+1),fileinfo[i][0],fileinfo[i][1],fileinfo[i][2])  	




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
<col width="30">
<col width="200">
  <col width="140">
  <col width="140">
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

webbrowser.open("%s%s%s" % (os.environ['HOME'],"/Desktop","/topfiles.html")) #This is used to automatically open the html file in browser

print "Success"








	
