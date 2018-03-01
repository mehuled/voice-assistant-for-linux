import os, shutil

directory = "%s%s" % (os.environ["HOME"],"/Desktop")

extensionDirectoryPath = "%s%s" %(os.environ["HOME"],"/Documents/")


files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]

extensionList = [] 


for f in files :
	
	if "." in f :
		
		extension = f[::-1].split(".")[0][::-1]

		if extension not in extensionList :
			
			extensionList.append(f[::-1].split(".")[0][::-1])
			
			newExtensionDirectory = "%s%s" %(extensionDirectoryPath,"%s%s" % (extension.upper(),"s"))
			
			try :
				os.makedirs(newExtensionDirectory)
	
			except OSError :
				
				print "Directory already existed so I moved the file in the existing directory"

		shutil.move(os.path.join(directory,f),"%s%s" %(extensionDirectoryPath,"%s%s" % (extension.upper(),"s")))	

		print "Success!"

	#print f[::-1].split(".")[0][::-1]
