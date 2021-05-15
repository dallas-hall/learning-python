#!/usr/bin/env python3

# https://docs.python.org/3/library/binascii.html
import binascii

hex_str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
flag_binary = binascii.unhexlify(hex_str)
print (flag_binary)

# https://docs.python.org/3/library/stdtypes.html#bytes.decode
flag = flag_binary.decode()
print(flag)

