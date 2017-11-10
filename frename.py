#!/usr/bin/python

import os, sys, re
from PIL import Image

count = 1

def usage():
	print "frename.py <DIR_NAME> <File_Prefix>"

def getSuffix(Ifile):
	m = re.match(".*\.(\w+)", Ifile)
	if m:
		return "." + m.group(1)

	return None

def renameFile(rdir, prefix):
	if not os.path.isdir(rdir):
		print "Invalid dir path.."
		return None

	for Ifile in os.listdir(rdir):
		Ifile = rdir + "/" + Ifile
		try:
			im = Image.open(Ifile)
			suffix = getSuffix(Ifile)
			global count
			if suffix:
                                if count > 9:
				    name = prefix + str(count) + suffix
                                else:
                                    name = prefix + "0" + str(count) + suffix
			else:
                                if count > 9:
				    name = prefix + str(count) + str(im.format)
                                else:
                                    name = prefix + "0" + str(count) + str(im.format)

			print "Rename ", Ifile, " --> ", name
			name = rdir + "/" + name
			os.rename(Ifile, name)
			count += 1
		except IOError as err:
			print "Invalid Image: ", str(Ifile)
			

def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print "Invalid number of arguments.."
		usage()
		return None

	rdir = ""
	prefix = ""

	if len(sys.argv) == 3:
		rdir = sys.argv[1]
		prefix = sys.argv[2]
	else:
		rdir = sys.argv[1]

	renameFile(rdir, prefix)

if __name__ == "__main__":
	main()
