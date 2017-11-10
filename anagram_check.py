#!/usr/bin/python

import sys

def insertDict( d, ch ):
	if ch in d:
		d[ch] += 1
	else:
		d[ch] = 1

def removeDict( d, ch ):
	if ch NOT in d:
		

def areAnagrams( str1, str2 ):
	if( len(str1) != len(str2) ):
		return False

	char_dict = dict()

	for ch in str1:
		char_dict['']	

def main():
	if len(sys.argv) != 3:
		print "Invalid Number of Args.."
		exit
	else:
		str1 = sys.argv[1]
		str2 = sys.argv[2]

	if( areAnagrams(str1, str2) ):
		print "String \'%s\' & String \'%s\' are Anagrams..", str1, str2

if __name__ == "__main__":
	main()
