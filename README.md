# orphan-scan

A script that scans all DITA files in a directory and reports those files that are not referenced by any other file DITA in that directory. Such a check is useful for identifying image files or content files that are not called by any of your DITA files.

## Usage instructions

#### Prerequisite

Download and install Python 2.7.5. Later versions of Python should also work.

#### Steps

1. Download this entire repository as a `.zip` file, extract the contents to any folder, and double-click `orphanscan.py`.
2. When prompted, enter the full path of the directory to be scanned, for example, `c:\documentation\`. Do not forget to enter the trailing `\` for the directory. 
3. When the checking is complete, you see a message on the console: `Press any key to exit.` Press any key. 
4. Go to the folder that contains the script. You see a file called `orphanScan.html`. This is the report file for you to read and act upon.

## Limitations

The script checks only `.dita` and `.ditamap` files. If your filenames have the `.xml`, `.html`, or `.xhtml` extension, this script will not work.

## Bugs and enhancements

Use GitHub's issue tracking feature.

## Licensing

The script is under [GPL 3](https://opensource.org/licenses/GPL-3.0), which is a copyleft licence. You are free to use and distribute this code as-is. You are also free to modify and distribute this code provided you distribute such modified code in its entirety under the same licence as this one, that is GPL 3.
