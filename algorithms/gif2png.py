__author__ = 'xxdpavelxx'

import glob
from PIL import Image

def gif2png():  #Should be run in a directory with at least 1 gif file.
    file_names = glob.glob("/directory/*.gif") #or use specific file name instead of * and directory name instead of 'directory'.
    for GIFS in file_names:
        print "Converting %s from PNG to GIF: "  %GIFS # will tell you what files are being converted
        try:
            pnger = Image.open(GIFS)
            pnger.save( "/directory_/", "png" )
        except Exception as exc:
            print "Error: " + str(exc)
