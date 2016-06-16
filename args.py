#import sys

from sys import argv

script_nm, runid,fcid = argv

if len(argv < 2):
	sys.exit ("Usage: %s <runid> <fcid>" % script_nm)
else:
	print "Assigning codes for runid: %r fcid %r" % (script_nm,fcid)
