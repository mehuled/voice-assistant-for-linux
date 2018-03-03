#from __future__ import division
import os, shutil
import webbrowser

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

html_body = ''

for i in xrange(10) :
	html_body =  "%s <tr> <td> %s </td> <td> %s MB </td> </tr>" %(html_body,fileinfo[i][0],fileinfo[i][1])  	



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
<col width="80">
  <col width="80">
  <tr>
    <th>Filename</th>
    <th>Size</th>
  </tr>'''
  
  
  
html_end = '''</table>

</body>
</html>
'''


Html_file= open("%s%s%s" % (os.environ['HOME'],"/Desktop","/topfiles.html"),"w")
Html_file.write("%s %s %s" % (html_start,html_body,html_end))
Html_file.close()

webbrowser.open("%s%s%s" % (os.environ['HOME'],"/Desktop","/topfiles.html"))

print "Success"








	
