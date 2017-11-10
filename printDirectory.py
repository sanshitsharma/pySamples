#!/usr/bin/python

import sys
import os

def print_directory_contents(sPath):
	for sChild in os.listdir(sPath):
		sChildPath = os.path.join(sPath, sChild)

		if os.path.isdir(sChildPath):
			print_directory_contents(sChildPath)
		else:
			print sChildPath

def main():
	if len(sys.argv) != 2:
		print "Invalid number of arguments"
		sys.exit()


	sPath = sys.argv[1]

	if os.path.isdir(sPath):
		print sPath
	else:
		print "Invalid Directory..!!"

	print_directory_contents(sPath)


if __name__ == "__main__":
	main()
