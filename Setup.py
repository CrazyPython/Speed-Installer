import urllib
import os
py2exe = "https://downloads.sourceforge.net/project/py2exe/py2exe/0.6.9/py2exe-0.6.9.win32-py2.6.exe?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpy2exe%2Ffiles%2F&amp;ts=1356117096&amp;use_mirror=superb-dca3"
f = open("py2exe")
print"Downloading py2exe installer..."
f.write(urllib.open(py2exe).read())
f.close()
print"Please Install py2exe"
os.system(os.getwd()+"py2exe")
