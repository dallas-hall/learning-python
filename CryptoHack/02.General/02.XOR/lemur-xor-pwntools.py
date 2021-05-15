#!/usr/bin/python3

# FIFTH CHALLENGE - elegant solution by https://cryptohack.org/user/shoaloak/

from PIL import Image
from pwn import *

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

# Get image binary - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.tobytes
lemur_pic_binary = lemur_pic.tobytes()
flag_pic_binary = flag_pic.tobytes()

# XOR the 2 images which gets us the input for the initial XOR
xor_result_binary = xor(lemur_pic_binary, flag_pic_binary)

# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.frombytes
xor_result_pic = Image.frombytes(flag_pic.mode, flag_pic.size, xor_result_binary)

# Save the result to a file - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save
xor_result_pic.save('xor_result.png')

# Same picture as above
# xor_result_pic = Image.frombytes(lemur_pic.mode, lemur_pic.size, xor_result_binary)
# xor_result_pic.save('xor_result.png')
