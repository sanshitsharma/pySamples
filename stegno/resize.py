import argparse 
import os
from PIL import Image

def resize(in_dir, out_dir, size):
    for a_file in os.listdir(in_dir):
        in_file = in_dir + "/" + a_file
        out_file = out_dir + "/" + a_file
        try:
            im = Image.open(in_file)
            if size < im.size:
                print "Resizing image", in_file, "to", size
                im.thumbnail(size)
            im.save(out_file, "JPEG")
        except IOError as err:
            print "file:", a_file, " is not an image"

def main():
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('input_dir', nargs=1, help='path to directory containing all images to be resized')
    parser.add_argument('size', nargs=1, help='new size format: 1024x768')
    parser.add_argument('--out_dir', '-o', nargs=1, help='path to directory where encoded files should be stored')

    args = parser.parse_args()
    print args
    in_dir = args.input_dir.pop()

    # Some checks can be done here
    size = tuple(map(int, args.size.pop().split("x")))
    if args.out_dir == None:
        out_dir = in_dir
    else:
        out_dir = args.out_dir.pop()
        if out_dir.endswith("/"):
            out_dir = out_dir[:-1]

    resize(in_dir, out_dir, size)


if __name__ == '__main__':
    main()
