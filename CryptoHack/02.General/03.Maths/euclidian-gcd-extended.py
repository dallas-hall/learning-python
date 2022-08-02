#!/usr/bin/python3

# SECOND CHALLENGE

import logging
import math
import os
import sys
import time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# https://www.mathsisfun.com/definitions/coefficient.html

# Let a and b be positive integers.
# The extended Euclidean algorithm is an efficient way to find integers u,v such that
#
# a * u + b * v = gcd(a,b)
#
# Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.
# Using the two primes p = 26513, q = 32321, find the integers u,v such that
#
# p * u + q * v = gcd(p,q)
#
# Knowing that p,q are prime, what would you expect gcd(p,q) to be?
# ANSWER: 1.

p = 26513
q = 32321


def gcdEuclidSubtractionRecursion(a, b):
	"""The Euclid subtraction algorithm works as follows.
1) Start with 2 numbers, a and b.
2) Find the difference between a and b (large -  small)
3) Repeat step 2 until a = b or both are 0. This is the GCD.
Many subtraction steps are necessary so it can be improved with division remainder."""
	if a == b:
		return a
	elif a > b:
		c = a - b
		recursionResult = gcdEuclidSubtractionRecursion(b, c)
	else:
		c = b - a
		recursionResult = gcdEuclidSubtractionRecursion(a, c)
	return recursionResult


def gcdEuclidModuloRecursion(a, b):
	"""The Euclid division remainder algorithm
1) Start with 2 numbers, a and b.
2) Reduce the large number. a is now b and b is now a % b.
3) Repeat 2 until the remainder is 0.
	"""
	if b == 0:
		return a
	else:
		c = a % b
		recursionResult = gcdEuclidModuloRecursion(b, c)
		return recursionResult


answer = gcdEuclidSubtractionRecursion(p, q)
print('gcdEuclidSubtractionRecursion answer: ' + str(answer))

answer = gcdEuclidModuloRecursion(p, q)
print('gcdEuclidModuloRecursion answer: ' + str(answer))

answer = math.gcd(p, q)
print('math.gcd answer: ' + str(answer))
