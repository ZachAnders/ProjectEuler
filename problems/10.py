#!/usr/bin/env pypy

from factor import get_factors

bound = 2000000

running_sum = 0

for i in xrange(2, bound):
	if len(get_factors(i)) == 1:
		running_sum += i
	if not (i%20000):
		print(i)
		
print(running_sum)
