#!/usr/bin/python

import os, argparse, sys

def usage():
	print 'usage: ' + os.path.basename(sys.argv[0]) + ' [-h] -in INFILE -k KEY [-o OUT]'

def get_dst(dst):
	if dst.endswith('enc') or dst.endswith('dec'):
		dst = dst[:len(dst)-4]

	return dst

def encrypt_file(src, dst, key):
	cmd = 'cat ' + src + ' | openssl rsautl -encrypt -pubin -inkey ' + key + ' > ' + dst
	rv = os.system(cmd)
	if not rv:
		print "Encryption Successful.. Encrypted file stored at " + dst
	else:
		print "Encryption Failed.."

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--infile', nargs=1, help='Path to source file..', required='true')
    parser.add_argument('-k', '--key', nargs=1, help='Public key to be used for encryption (.pub.pem) extension', required='true')
    parser.add_argument('-o', '--out', nargs=1, help='Destination file/directory where the out file will be stored')

    args = parser.parse_args()

    # Parse the input file argument
    if args.infile[0] == "":
        print "error: argument -in/--infile expects a valid filepath"
        usage()
        sys.exit(1)
    srcfile = args.infile[0]

    # Parse the public key
    if args.key[0] == "":
        print "error: argument -k/--key expects a valid public key file"
        usage()
        sys.exit(1)
    key = args.key[0]

    # Parse the output file argument
    if args.out is not None:
        dstfile = args.out[0]
        if os.path.isdir(dstfile):
            dstfile = dstfile + get_dst(os.path.basename(srcfile)) + '.enc'
    else:
        dstfile = get_dst(srcfile) + '.enc'

    #encrypt_file(srcfile, dstfile, key)

    print srcfile
    print dstfile
    print key
	

if __name__ == '__main__':
	main()
