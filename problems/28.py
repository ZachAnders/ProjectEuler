#!/usr/bin/env pypy

import factor

def iter_primes(a, b):
	n = 0
	while True:
		yield (n**2) + (a*n) + b
		n += 1

def is_prime(n):
	return n >= 0 and len(factor.get_factors(n)) == 1

max_counter = 0
max_val = (0, 0, 0)

for a_val in xrange(-999, 1000):
	for b_val in xrange(-999, 1000):
		num_gen = iter_primes(a_val, b_val)
		counter = 0
		while is_prime(num_gen.next()):
			counter += 1
		if counter > max_counter:
			print("Found new max: a: %d, b: %d num primes: %d" % (a_val, b_val, counter))
			max_counter = counter
			max_val = (a_val, b_val, counter)

print("a: %d, b: %d num primes: %d" % max_val)
