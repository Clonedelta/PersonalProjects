###############################################################################
# chunk_generator.py main file
# Runs through the list of mp3's you have and uses 
# dandev-el3.exe to convert them at once
# Author: Clonedelta
###############################################################################

#Import Statements here
import os
import sys

ANSI_COLOR_YELLOW = "\x1b[33m"
ANSI_COLOR_GREEN = "\x1b[32m"
ANSI_COLOR_RESET = "\x1b[0m"


# gets the current directory
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/Input"

# loops through the current directory
for soundName in os.listdir(dir_path):
	if soundName.endswith(".mp3"):

		#print "Before: " + soundName
		chunkName = soundName[:-4] + ".chunk"
		
		print ANSI_COLOR_YELLOW + "Converting file " + ANSI_COLOR_GREEN + soundName + ANSI_COLOR_RESET
		os.system("./dandev-el3.exe " + "Input/" + soundName + " -o " + " Output/" + chunkName)
		print "-----------------------------------------------------------------------------\n"
		
print 'wictoe is cwinge uwu'