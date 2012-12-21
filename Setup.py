import urllib
import os
clipboard = "https://sites.google.com/site/cyke642/clipboard.py?attredirects=0"
py2exe = "https://downloads.sourceforge.net/project/py2exe/py2exe/0.6.9/py2exe-0.6.9.win32-py2.6.exe?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpy2exe%2Ffiles%2F&amp;ts=1356117096&amp;use_mirror=superb-dca3"
f1 = open("py2exe")
print"Downloading py2exe installer..."
f1.write(urllib.open(py2exe).read())
print"Py2exe download finished."
f1.close()
f2 = open("clipboard")
print"Downloading clipboard"
f2.write(urllib.open(clipboard).read())
print"Clipboard download finished."
f2.close()
print"Please Install py2exe"
os.system(os.getwd()+"py2exe")
raw_input("Setup finished,Press enter to exit.")
