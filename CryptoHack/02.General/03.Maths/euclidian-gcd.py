#!/usr/bin/python3
import logging
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

# https://www.mathsisfun.com/definitions/coprime.html
# https://en.wikipedia.org/wiki/Euclidean_algorithm
# https://github.com/blindcant/c/blob/master/C-How-To-Program/Chapter05/greatest-common-divisor.c

# The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).
# For a = 12, b = 8 we can calculate the divisors of a: {1,2,3,4,6,12} and the divisors of b: {1,2,4,8}. Comparing these two, we see that gcd(a,b) = 4.
# Now imagine we take a = 11, b = 17. Both a and b are prime numbers. As a prime number has only itself and 1 as divisors, gcd(a,b) = 1.
# We say that for any two integers a,b, if gcd(a,b) = 1 then a and b are coprime integers.
# If a and b are prime, they are also coprime. If a is prime and b < a then a and b are coprime.
# Think about the case for a prime and b > a, why are these not necessarily coprime?
# ANSWER: ???
# There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.
# Try coding it up; it's only a couple of lines. Use a = 12, b = 8 to test it.
# Now calculate gcd(a,b) for a = 66528, b = 52920 and enter it below.
a = 66528
b = 52920


def gcdEuclidSubtractionRecursion(n, m):
	"""The Euclid subtraction algorithm works as follows.
1) Start with 2 numbers, a and b.
2) Find the difference between a and b (large -  small)
3) Repeat step 2 until a = b or both are 0. This is the GCD.
Many subtraction steps are necessary so it can be improved with division remainder."""
	recursionResult = 0
	o = 0
	if n == m:
		return n
	elif n > m:
		o = n - m
		recursionResult = gcdEuclidSubtractionRecursion(m, o)
	else:
		o = m - n
		recursionResult = gcdEuclidSubtractionRecursion(n, o)
	return recursionResult


def gcdEuclidModuloRecursion(n, m):
	"""The Euclid division remainder algorithm
1) Start with 2 numbers, a and b.
2) Reduce the large number. a is now b and b is now a % b.
3) Repeat 2 until the remainder is 0.
	"""
	if m == 0:
		return n
	else:
		o = n % m
		recursionResult = gcdEuclidModuloRecursion(m, o)
		return recursionResult

answer = gcdEuclidSubtractionRecursion(a,b)
print('gcdEuclidSubtractionRecursion answer: ' + str(answer))

answer = gcdEuclidModuloRecursion(a,b)
print('gcdEuclidModuloRecursion answer: ' + str(answer))
