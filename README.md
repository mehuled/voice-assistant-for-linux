# unclutter-desktop-alexa-innovaccer

## This is a project for Hacker Camp 018 by Innovaccer.

#### Lambda Function ARN : arn:aws:lambda:us-east-1:372942179917:function:mehulsGirlfriendOnAlexa


## Features
* Unclutter any directory from *desktop*, *documents*, *downloads*, *music*, *videos*, *pictures*  by moving files based on thier extensions in different folders of names similar to extensions for example all pdf files are moved in a folder *PDFs* in */Documents*. Just provide the name of the directory to be uncluttered as a command line argument to the script `unclutter.py` .
* List top n files on the system based on size. ( n = 10 by default, n is accepted as a command line argument)
* Your computers own history. List n files based on time of most recent access. (Pass argument 'lat' to the script topfilesbysize.py)
* Delete old unused files on the system. List n most earliest accessed files on the system by providing the command line argument 'eat' which by default provides the top 10 files with earliest access times, Provide command line argument '50 eat' to list top 50 files with earlist access time. 
* Voice controlled by Alexa, Created an Alexa skill to setup a remote connection to the system by running a lambda function and then execute commands by giving instructions to your echo device like, 'Alexa, Unclutter my desktop', 'Alexa, list top files by size'. Please find the attached video for demo. Below infrastructure map shows how Alexa skill to execute commands using your echo device works.



<img src="https://github.com/mehuled/unclutter-desktop-alexa-innovaccer/blob/features/alexaworksFinal.png" width="910" height="364" />
