from __future__ import absolute_import

import os 
import re 
import stat
import random 
import tempfile
import fileinput
import os.path


from sys import argv

__outputter__ = {
    'tree' : 'txt',
    }
    
__ALIAS_RE = re.compile(r'([^:#]*)\s*:?\s*([^#]*?)(\s+#.*|$)')

script, fileName = argv


if (os.path.isfile(fileName)):
	if (480000 > os.stat(fileName).st_size):
		file1 = open("fileToText.txt", "w")
		for line in fileinput.input(fileName):
			file1.write(line)
		file1.close()
	else:
		print "file is over 500KB, the is too large."
else: 
	print "The file does not exist."

