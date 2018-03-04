import os, shutil
import sys



if len(sys.argv) == 1 :
	directoryToUnclutter = "/Desktop"

elif len(sys.argv) == 2 :
	
	
	if (sys.argv[1]).lower() in ['documents','music','videos','downloads','pictures'] :
		directoryToUnclutter = "/%s" %((sys.argv[1]).lower().title())	
	
	else :
		print "Invalid Argument. Running in default mode."
		directoryToUnclutter = "/Desktop"



else :
	print "Too many arguments provided. Running in default mode!"
	directoryToUnclutter = "/Desktop"



directory = "%s%s" % (os.environ["HOME"],directoryToUnclutter)

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
		
		
		try :
			shutil.move(os.path.join(directory,f),"%s%s" %(extensionDirectoryPath,"%s%s" % (extension.upper(),"s")))	


		except shutil.Error :
		
			print " %s , file with same name already present in the directory so not moving." %(f)
		
		print "Success!"

	#print f[::-1].split(".")[0][::-1]
