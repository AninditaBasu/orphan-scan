# orphan-scan

A script that scans all DITA files in a directory and reports those files that are not referenced by any other file DITA in that directory. Such a check is useful for identifying image files or content files that are not called by any of your DITA files.

## Usage scenario

You have several image files, topic files, and other files in the directory but hesitate to delete them because you are not sure if any of these files are referenced by the DITA files in that directory. You tell the script which directory it should scan. The script runs the checks and gives you a report that you can read and act upon to clean up your workspace.

## Documentation

See [Anin's Documentation Tools](https://doc-tools.readthedocs.io/en/latest/).
 
## Limitations

It is assumed that all DITA topic files have the `.dita` extension. If your files use the `.xml` extension, this script will not work in its present form.

## Acknowledgments

The code was converted from .py to .exe through [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe).

## Licensing

The script is under [GPL 3](https://opensource.org/licenses/GPL-3.0), which is a copyleft licence. You are free to use and distribute this code as-is. You are also free to modify and distribute this code provided you distribute such modified code in its entirety under the same licence as this one, that is GPL 3.