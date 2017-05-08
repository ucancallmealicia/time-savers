#Python 3

#This script loops through a given directory and copies certain files to a new directory
#Probably only works for Windows machines

import os
import shutil

#make sure to include full path, i.e. C:\Users\username\Desktop\inputfolder
olddirectory = input('List the directory path to the files you want to copy: ')
#make sure to include full path, i.e. C:\Users\username\Desktop\outputfolder
newdirectory = input('List the output directory path: ')
#include only the filename and extension (it already knows the directory); include comma and space between each file name
files_to_copy = input('List the files you want to copy, including extension (i.e. file01.txt, file02.xml, etc.): ')

#creates a list of filenames to compare to input directory
files_list = list(map(str,files_to_copy.split(',')))
new_files_list = [x.strip(' ') for x in files_list]

#pulls input directory list
directorylist = os.listdir(olddirectory)

#readies the log file
log = newdirectory + '\\' + 'log.txt'
logfile = open(log, 'w')

#loops through input file list and copies matching files to new directory, or logs an error
for i in new_files_list:
        if i in directorylist:
                shutil.copy(olddirectory + '\\' + i, newdirectory)
                print('Success! ' + i + ' has been moved to the new directory')
                logfile.write(i + ' has been moved to the new directory' + '\n')
        else:
                print('Error! ' + i + ' not found in directory')
                logfile.write(i + ' not found in directory' + '\n')
#closes log file
logfile.close()

#Done!
print('Done! Check log file in output directory for details')





