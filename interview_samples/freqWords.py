#!/usr/bin/python

from collections import Counter

try:
	with open('/Users/sansshar/Documents/perl_progs/tarun/samplepara.txt', 'r') as fr:
		lines = fr.read()
		wlst = lines.split()
		print Counter(wlst).most_common(5)
except Exception as err:
	print "Couldn't read file.."

