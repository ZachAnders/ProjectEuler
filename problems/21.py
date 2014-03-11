#!/usr/bin/env pypy

import factor

def d(n):
	factors = factor.get_factors(n)
	am_nums = []
	for pair in factors:
		if n in pair:
			am_nums.append(1)
		else:
			am_nums += pair
	return sum(am_nums)
	
running_sum = 0

for i in xrange(0, 10000):
	if d(d(i)) == i and d(i) != i:
		running_sum += i
		print "d(%d) == %d d(%d) = %d" % (i, d(i), d(i), d(d(i)))

print(running_sum)
