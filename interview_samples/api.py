#!/usr/bin/python

import urllib2, json, argparse

locu_api = 'ac8ad67cfce7dc26b4cbc1d07d512cdd39541842'

def locu_search(locality, category):
	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key

	final_url = url
	if locality:
		locality = locality.replace(' ', '%20')
		final_url = url + '&locality=' + locality

	if category:
		category = category.replace(' ', '%20')
		final_url = final_url + '&category=' + category

	print "URL: " + final_url

	json_obj  = urllib2.urlopen(final_url)
	data = json.load(json_obj)

	for item in data['objects']:
		print item

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--locality', nargs=1, required='true', help='Locality in which you want to search')
	parser.add_argument('-c', '--category', nargs=1, help='Search category (restaurant etc..)')

	args = parser.parse_args()

	locality = None
	category = None

	#Parse Locality
	if args.locality[0] != "":
		locality = args.locality[0]

	if args.category and args.category[0] != "":
		category = args.category[0]

	locu_search( locality, category ) 

if __name__ == "__main__":
	main()
