#!/usr/bin/python

import os, time, argparse, sys

def decrypt_file(src, dst):
	cmd = 'cat ' + src + ' | openssl rsautl -decrypt -inkey ~/.ssh/id_rsa > ' + dst
	rv = os.system(cmd)
	if not rv:
		print "Decryption Successful.. Decrypted file stored at " + dst
	else:
		print "Decryption Failed.."

def encrypt_file(src, dst):
	cmd = 'cat ' + src + ' | openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pub.pem > ' + dst
	rv = os.system(cmd)
	if not rv:
		print "Encryption Successful.. Encrypted file stored at " + dst
	else:
		print "Encryption Failed.."

def get_dst(dst):
	if dst.endswith('enc') or dst.endswith('dec'):
		dst = dst[:len(dst)-4]

	return dst	

def usage():
	print 'usage: ' + os.path.basename(sys.argv[0]) + ' [-h] --encrypt/--decrypt -in INFILE [-o OUT]'

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--encrypt', action='store_true')
	parser.add_argument('--decrypt', action='store_true')
	parser.add_argument('-in', '--infile', nargs=1, help='Path to source file..')
	parser.add_argument('-o', '--out', nargs=1, help='Destination file/directory where the out file will be stored')

	args = parser.parse_args()

	# Parse the action
	if args.encrypt:
		is_encrypt = True
		ext = '.enc'
	elif args.decrypt:
		is_encrypt = False
		ext = '.dec'
	else:
		print "error: invalid action type.."
		usage()
		sys.exit(1)

	# Parse the input file argument
	if args.infile is None or args.infile[0] == "":
		print "error: argument -in/--infile expects a valid filepath"
		usage()
		sys.exit(1)
	srcfile = args.infile[0]

	# Parse the output file argument
	if args.out is not None:
		dstfile = args.out[0]
		if os.path.isdir(dstfile):
			dstfile = dstfile + get_dst(os.path.basename(srcfile)) + ext
	else:
		dstfile = get_dst(srcfile) + ext

	if is_encrypt:
		encrypt_file(srcfile, dstfile)
	else:
		decrypt_file(srcfile, dstfile)

if __name__ == '__main__':
	main()
