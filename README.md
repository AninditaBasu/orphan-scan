# orphan-scan
A script that scans all files in a directory, recursively, and reports those files that are not referenced by any other file in that directory. Useful if you need to identify image files or content files that are not called by any of your DITA files.

To run the script, you need Python 2.7.5. Download and install Python from www.python.org. Doing so neither takes too long nor is difficult. You need it only to run the script; you don't need to know Python to run the script.

Usage instructions 1. Download the script to any folder on your computer. 2. Double-click the script. When prompted, enter the full path of the directory to be scanned, for example, c:\documentation. Do not forget to enter the trailing \ for the directory. 3. When the checking is complete, you see a message on the console: "Press any key to exit." Press any key. 4. Go to the folder where you saved the script. You see a file called orphanScan.html. This is the report file for you to read and act upon.

Limitations The script checks only .dita and .ditamap files for references to other files. If your content is authored in .xml, .html, or .xhtml format, this script will not work.

