###############################################################################
# gameCodeAdder.py main file
# Parses the filenames of the steam screenshots
# Author: Colin Smith
###############################################################################

#Import Statements here
import os
import sys

# gets the current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# print 'Before: '
# loops through the current directory
for filename in os.listdir(dir_path):
	if filename.endswith(".png") or filename.endswith(".jpg"):

		filePathArray = dir_path.split("/")
		
		parentFolder = filePathArray[len(filePathArray)-1]
		
		parentFolderSplit = parentFolder.split(" ")
		
		gameId = parentFolderSplit[len(parentFolderSplit)-1]
		
		gameId += "_"
		
		newFileName = gameId + filename
		
		os.rename(filename, newFileName)
		continue
	else:
		continue



# print 'After: '
# for filename in os.listdir(dir_path):
#     if filename.endswith(".png"):
#         print(filename[0])
#         print(os.path.join(filename))
#         continue
#     else:
#         continue
