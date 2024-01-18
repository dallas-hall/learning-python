#!/usr/bin/env python3

print("# Whitespace Examples")
print('" Python"')
# Tab
print('"\tPython"')
# Newline (Linux)
print('"\nPython"')
# Carriage return (Mac)
print('"\rPython"')
# Carriage return and newline (Windows)
print('"\r\nPython"')

print("\n# Removing Whitespace Examples")
message = " Python "
# We are not reassigning the value of message so the stripping is only for printing.
print('"' + message.rstrip() + '"') # Right strip only.
print('"' + message.lstrip() + '"') # Left strip only.
print('"' + message.strip() + '"') # Strip both sides.
print('"' + message + '"')
