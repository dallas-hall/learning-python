#!/usr/bin/python3

# FIFTH CHALLENGE - elegant solution by https://cryptohack.org/user/Daneallen/

import logging
import os
import sys
import time

from PIL import Image

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# Open the image - https://pillow.readthedocs.io/en/stable/reference/Image.html#open-rotate-and-display-an-image-using-the-default-viewer
# & https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
lemur_pic = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")
flag_pic = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")

# Get the pixels of the images - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.load
# https://pillow.readthedocs.io/en/stable/reference/PixelAccess.html#pixelaccess
lemur_pixels = lemur_pic.load()
flag_pixels = flag_pic.load()

# Get the image size, in pixels. The size is given as a 2-tuple (width, height). So we can loop through them.
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.size
for i in range(lemur_pic.size[0]):  # for every pixel:
	for j in range(lemur_pic.size[1]):
		# Gather each RGB pixel
		lemur_pixel = lemur_pixels[i, j]
		flag_pixel = flag_pixels[i, j]

		# XOR each part of the pixel tuple
		red_pixel = lemur_pixel[0] ^ flag_pixel[0]
		green_pixel = lemur_pixel[1] ^ flag_pixel[1]
		blue_pixel = lemur_pixel[2] ^ flag_pixel[2]

		# Store the resulatant tuple back into an image
		flag_pixels[i, j] = (red_pixel, green_pixel, blue_pixel)

flag_pic.save("xor_result.png")
