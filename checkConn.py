#!/usr/bin/python

import urllib2, time

drop_count = 0

def internet_on():
	try:
		reponse = urllib2.urlopen('http://www.google.com', timeout=3)
		return True
	except urllib2.URLError as err:
		global drop_count
		drop_count += 1
		pass

	return False

def main():
	outfile = '/Users/sansshar/Documents/perl_progs/internet_drops.txt'
	while(True):
		if ( not internet_on() ):
			try:
				with open(outfile, "w") as fw:
					global drop_count
					fw.write(str(drop_count))
					break
			except Exception as e:
				print str(e)
				break

		time.sleep(30)

if __name__ == "__main__":
	main()
