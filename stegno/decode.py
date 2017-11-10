from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
import argparse
import os
import collections
import sys
import time
from PIL import Image

def decode_images(in_dir):
    # Verify that in_dir path is valid
    if not os.path.isdir(in_dir):
        print "in_dir path is invalid.."
        return None

    # Count number of image files in in_dir
    num_image_files = 0
    files = []
    for a_file in os.listdir(in_dir):
        a_file = in_dir + "/" + a_file
        try:
            im = Image.open(a_file)
            files.insert(num_image_files, a_file)
            num_image_files += 1
        except IOError as err:
            print "file:", a_file, " is not an image"

    msg = ""
    num_files = len(files)
    count = 1
    print ""
    for a_file in files:
        secret_text = Steganography.decode(a_file)
        if secret_text != None:
            print "Decoded", count ,"of", num_files, "files..."
            count = count + 1
            msg += secret_text

    print "\nHere's your message...\n\n"
    inp = raw_input("\nOK.. I have decoded the files.. Do you want to see your message?\n\n")
    if inp == 'y' or inp == 'yes':
        print
        print
        print "######", msg, "######"

    last_inp = raw_input("\nPSST.. !! Do you want me to tell you one more secret before I exit..?\n\n")
    if last_inp == 'y' or last_inp == 'yes':
        print "GO look at http://localhost:7885/static/index.html"
    
    

def delivery_prompt():
    print "\n***********************************************"
    print "Hey Ruhi..!!! Sanshit has asked me to deliver"
    print "a message to you.. He has encoded the messages"
    print "in some image files.."
    print ""
    print "Would you like me to decode it for you?? "
    print "***********************************************\n"

def main():
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('input_dir', nargs=1, help='path to directory containing encoded images') 

    args = parser.parse_args()
    in_dir = args.input_dir.pop()

    ans = raw_input("Hi!! Is this Ruhi?\n\n")
    if ans == 'y' or ans == 'yes':
        delivery_prompt()
        inp = raw_input("")
        if inp == 'y' or inp == 'yes' or inp == 'sure':
            msg = decode_images(in_dir)
        else:
            print("OK. No problem.. Come back when you want to see your message.. ")
            sys.exit()
    else:
        print ("Sorry.. This message is for Ruhi only.. Can't decode it for you.. ")

if __name__ == '__main__':
    main()
