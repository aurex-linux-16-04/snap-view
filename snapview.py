#! /usr/bin/python
# -*- coding: utf-8 -*-

import cv
import sys
import getopt
import os

def usage(param=''):
	if param:
		print param

	print 'Usage: '+sys.argv[0]+' [-t TIME] [-f] FILE'
	sys.exit()

def clear_tmpfiles():
    filelist = glob.glob(imagefile + "*.jpg")
    for f in filelist:
        os.remove(f)	

        
if __name__ == '__main__':
	
	follow = False
	timelapse = 5

	try:
		opts, img_files = getopt.getopt(sys.argv[1:], "hft:", ["help", "follow", "time="])
	except getopt.GetoptError:
		usage()
                sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
		elif opt in ( "-f", "--follow"):
			follow = True
		elif opt in ( "-t", "--time"):
			timelapse = int(arg)

	if not img_files:
		usage()

	img_file = img_files[0]
	if not os.path.isfile(img_file):
		usage(img_file+" not found")

	print img_file
	runShow = True
	escShow = False

	showtime = 0
	(x, y) = (0, 0)
        image_cv = cv.LoadImage(img_file)
        cv.ShowImage(img_file, image_cv)
	cv.MoveWindow(img_file, x, y)
	while runShow:
        	image_cv = cv.LoadImage(img_file)
        	cv.ShowImage(img_file, image_cv)
		c = cv.WaitKey(timelapse*1000) % 256
		if c == 27:
			# ESC pressed. Finish the program
			follow = False

		runShow = follow

	cv.DestroyWindow(img_file)

