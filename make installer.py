"Version 1: simple DOS style creator"
import clipboard,os
URL = raw_input("Download URL (see Troubleshooting for Sourceforge):")
name = raw_input("name:")
if URL == char(22):
  URL = clipboard.get()
f = open("Installer.py")
code = """
import urllib,os
os.mkdir("C:/Program Files/{0}")
f = open("C:/Program Files/{0}")
f.write(urllib.open("{1}.zip").read())
zip = ZipFile('C:/Program Files/{0}.zip')
zip.extractall()
os.remove("C:/Program Files/{0}.zip")
""".format((name,URL))
f.write(code)
f.close()
setup = """
from distutils.core import setup
import py2exe
setup(console=['Installer.py'])
"""
f = open(setup.py)
f.write(setup)
f.close()
os.system("py2exe"+"python "+"os.getwd()"+"setup.py py2exe")
