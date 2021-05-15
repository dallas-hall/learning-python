#!/usr/bin/python3

# FIFTH CHALLENGE

import logging
import os
import sys
import time

# https://pypi.org/project/Pillow/
from PIL import Image, ImageChops

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# I've hidden two cool images by XOR with the same secret key so you can't see them!
lemur_pic = 'lemur_ed66878c338e662d3473f0d98eedbd0d.png'
flag_pic = 'flag_7ae18c704272532658c10b5faad06d74.png'

# Note: I initially tried doing this with binary myself but failed. I cheated and looked at someone else's solution
# and realised I was doing the right operation but with the wrong tools.
# https://github.com/jg-rivera/cryptohack/blob/master/general/xor/lemur_xor/lemur_xor.py
# https://stackoverflow.com/a/54400116

# Open the image - https://pillow.readthedocs.io/en/stable/reference/Image.html#open-rotate-and-display-an-image-using-the-default-viewer
# & https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
with Image.open(lemur_pic) as file:
	# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
	# 1 bit pixels needed for XOR - https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
	image1 = file.convert("1")

with Image.open(flag_pic) as file:
	# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
	# 1 bit pixels - https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
	image2 = file.convert("1")

# XOR the pictures - https://pillow.readthedocs.io/en/stable/reference/ImageChops.html#PIL.ImageChops.logical_xor
xor_result = ImageChops.logical_xor(image1, image2)

# Save the result to a file - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save
# The problem here is we lost the colour, so it is unreadable.
xor_result.save("xor_result.png")

# Using ImageMagick solves the colour loss solution.
# convert flag_7ae18c704272532658c10b5faad06d74.png lemur_ed66878c338e662d3473f0d98eedbd0d.png -evaluate-sequence xor result.png
