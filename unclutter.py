import os, shutil
import sys

#------------------- This is to handle the command line arguments provided----------------------

if len(sys.argv) == 1 :
	directoryToUnclutter = "/Desktop"

elif len(sys.argv) == 2 :
	
	
	if (sys.argv[1]).lower() in ['documents','music','downloads','pictures','movies','videos'] :
		directoryToUnclutter = "/%s" %((sys.argv[1]).lower().title())	
	
	else :
		print ("Invalid Argument. Running in default mode.")
		directoryToUnclutter = "/Desktop"



else :
	print ("Too many arguments provided. Running in default mode!")
	directoryToUnclutter = "/Desktop"



directory = "%s%s" % (os.environ["HOME"],directoryToUnclutter)

#--------------This is to set the path of the directory where new folders based on extensions will be created------------------

extensionDirectoryPath = "%s%s" %(os.environ["HOME"],"/Documents/")   

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]

extensionList = [] 

#--------------- This is to look for all the files in the directory to be uncluttered-----------------

for f in files :
	
	if "." in f :                  #To move only those files which have a extension
		
		extension = f[::-1].split(".")[0][::-1]

		if extension not in extensionList :
			
			extensionList.append(f[::-1].split(".")[0][::-1])
			
			newExtensionDirectory = "%s%s" %(extensionDirectoryPath,"%s%s" % (extension.upper(),"s"))
			
			try :
				os.makedirs(newExtensionDirectory)
	
			except OSError :
				
				print ("Directory already existed so moved the file in the existing directory")
		
		
		try :
			shutil.move(os.path.join(directory,f),"%s%s" %(extensionDirectoryPath,"%s%s" % (extension.upper(),"s")))	


		except shutil.Error :
		
			print (" %s , file with same name already present in the directory so not moving." %(f))
		
		print ("Successfully Uncluttered!")

	
