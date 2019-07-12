#
#
# orphanscan.py
# Copyright (C) 2015  Anindita Basu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.txt.
#
#
import os
#
# Open a file called "orphanScan.html" to write the findings to.
#
reportfile = open("orphanScan.html", "w")
reportfile.write("<html>")
reportfile.write("<head>")
reportfile.write("<title>Search report</title>")
reportfile.write("<style>h1{color:#A52A2A;}")
reportfile.write("h2{color:#A52A2A;}")
reportfile.write("h3{color:#A52A2A;}")
reportfile.write("h4{color:#A52A2A;}")
reportfile.write('p{font-family:"Trebuchet MS", Arial, Verdana, serif; font-size:16px;line-height:120%;}')
reportfile.write('li{font-family:"Trebuchet MS", Arial, Verdana, serif; font-size:16px;line-height:200%;}')
reportfile.write('td{font-family:"Trebuchet MS", Arial, Verdana, serif; font-size:16px;line-height:200%;}</style>')
reportfile.write("</head>")
reportfile.write("<body>")
reportfile.write("<h1>Orphan report</h1>")
#
#
# Get the directory that contains the DITA files.
#
print ('\nSpecify the full path of the directory to be scanned, for example, C:\jazz_repo\prodA\\\n')
print ('Do not forget the trailing slash\n')
#
workspace = input("Enter the full path of directory to be scanned: ")
#
reportfile.write('<p>Directory scanned: <a href = "file:///')
reportfile.write(workspace)
reportfile.write('" target = "_blank">')
reportfile.write(workspace)
reportfile.write("</a></p>")
reportfile.write("<hr/>")
#
#
# start a counter for the number of subfolders in the directory
#
counter = 0
#
# Print out the subfolders. Also, count them and print out the count.
#
print ('\nReading the directory ...\n')
#
try:
    for foldername in os.listdir(workspace):
        counter += 1
        print (foldername)
except:
    print ('The directory could not be found.\n')
    exit()
print ('\nThe program will scan these', counter, 'folders in the', workspace, 'directory.\n')
#
# Start a counter to count ALL files in the directory
#
counter = 0
#
# Traverse the directory and create a list of ALL files
#
bigfilelist = []
for (dirname, dirs, files) in os.walk(workspace):
    for filename in files:
        counter += 1
        bigfilelist.append(filename)
        #print (filename)
print ('\n',counter, 'files in the directory.\n')
#
# Start a counter for the number of .dita and .ditamap files in the directory
# If file is a .dita or .ditamap file, create the full file path,
# and add to a smaller file list.
#
counter = 0
smallfilelist = []
for (dirname, dirs, files) in os.walk(workspace):
    for filename in files:
        if filename.endswith('.dita') or filename.endswith('.ditamap'):
            counter += 1
            thefile = os.path.join(dirname, filename)
            smallfilelist.append(thefile)
            #print (thefile)
print ('\n',counter, 'content files (.dita and .ditamap).\n')
#
# Traverse bigfilelist, check if list item exists in contents of file in smallfilelist
# If not exists, list item is an orphan. Print it out.
#
print ('These are the files that are not called by any other file in this directory:')
reportfile.write('<p>These are the files that are not called by any other file in this directory:</p>')
reportfile.write('<ul>')
#
filefound = 0
for fname in bigfilelist:
    for contentfile in smallfilelist:
        handle = open(contentfile, 'r', encoding='ISO-8859-2')
        filecontent = handle.read()
        if fname in filecontent:
            filefound += 1 # if file is referenced, increment the counter
        handle.close()
    if filefound == 0:
        reportfile.write('<li>')
        print (fname) # if counter is still zero, file isn't referenced by smallfilelist
        reportfile.write(fname)
        reportfile.write('</li>')
    filefound = 0 #re-initialise the counter
#
reportfile.write('</ul><hr\>')
# print a completion message
#
print ('Finished scanning the directory.')
#
# Write the closing HTML tags in the report file.
#
reportfile.write("</body>")
reportfile.write("</html>")
reportfile.close()
#
# Wait for user input so that a person gets enough time to read whatever's been printed on the console
# and then close the program
#
print ("The program will now end.")
input("Press any key to close.")
exit()
