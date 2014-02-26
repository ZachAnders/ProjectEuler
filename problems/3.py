#!/usr/bin/env pypy
import math

composite = 600851475143

def get_factors(val):
	factors = []
	for i in xrange(3, int(math.ceil(math.sqrt(val))), 2):
		if val % i == 0:
			factors.append(i)
			factors.append(val/i)
	return factors
all_factors = get_factors(composite)
print all_factors
prime_factors = [factor for factor in all_factors if len(get_factors(factor)) == 0]
print prime_factors
print max(prime_factors)
