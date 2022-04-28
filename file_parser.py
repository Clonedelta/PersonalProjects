###############################################################################
# file_parser.py main file
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

        pFname = list(filename)
        p = pFname.index("_")  # find position of "_"

        for i in range(0,p+1):
            del(pFname[0])         # delete it

        parsedFName = ''.join(pFname)
        # print(os.path.join(filename))
        # print(parsedFName)

        os.rename(filename, parsedFName)
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
