#!/usr/bin/env python

url = 'https://nostarch.com/'
print(url)
print(url.removeprefix('https://'))
print(url.removesuffix('/'))
print(url.removeprefix('https://'))
print(url.removeprefix('https://').removesuffix('/'))