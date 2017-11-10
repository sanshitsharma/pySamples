# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
import argparse
import os
import collections
from PIL import Image

"""
# hide text to image
path = "/Users/sansshar/Documents/python_progs/stegno/V_Select/Blue_Fool.jpg"
output_path = "/Users/sansshar/Documents/python_progs/stegno/v_images/Blue_Foool.jpg"
text = 'The quick brown fox jumps over the lazy dog.'
Steganography.encode(path, output_path, text)

# read secret text from image
secret_text = Steganography.decode(output_path)
print secret_text
"""

def update_map(msg_map, key, value):
    #print "Inserting", key, ":", value, " to map"
    if key in msg_map.keys():
        file_list = msg_map[key]
        file_list.append(value)
        msg_map[key] = file_list
    else:
        msg_map[key] = [value]

    return msg_map

def encode(text, files, out_dir):
    for in_file in files:
        out_file = out_dir + "/" + os.path.basename(in_file)
        Steganography.encode(in_file, out_file, text)

def encode_images(in_dir, out_dir, message):
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

    if num_image_files == 0:
        print "no image files found in input dir"
        return None

    # Message length
    msg_len = len(message)

    delta = num_image_files - msg_len
    print delta

    msg_map = collections.OrderedDict()
    idx = 0

    if delta >= 0:
        # number of images is greater than or equal to
        # number of chars. given 'n' characters in the 
        # message, pick the first n images and encode
        # 1 character in each image
        for i in range(msg_len):
            msg_map = update_map(msg_map, message[i], files[i])
    else:
        # number of images is less than. we need to do
        # some smart mapping here. use the delta to find
        # out how many extra chars we have and then 
        # pack the remaining chars in the last file
        one_to_one = delta - 1
        for i in range(msg_len + one_to_one):
            msg_map = update_map(msg_map, message[i], files[i])
            idx = i

        print "idx after loop =", idx
        msg_map[message[idx+1:]] = files[idx+1]

    """
    for key in msg_map.keys():
        print key, ":", msg_map[key]
    """

    # Now that we have the map, all we need to do is encode the
    # text into each file
    for key in msg_map.keys():
        print "Encoding...", key, " to files:", msg_map[key]
        encode(key, msg_map[key], out_dir)

def main():
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('input_dir', nargs=1, help='path to directory containing all images to be encoded')
    parser.add_argument('--out_dir', '-o', nargs=1, help='path to directory where encoded files should be stored')

    args = parser.parse_args()
    in_dir = args.input_dir.pop()
    if args.out_dir == None:
        out_dir = in_dir
    else:
        out_dir = args.out_dir.pop()
        if out_dir.endswith("/"):
            out_dir = out_dir[:-1]

    message = "HAPPY 32nd BIRTHDAY, RUHI!!" 
    encode_images(in_dir, out_dir, message)


if __name__ == '__main__':
    main()
