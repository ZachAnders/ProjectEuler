#!/usr/bin/env pypy

import factor

memo_a = {}
def is_abundant(n):
	if n not in memo_a:
		factors = factor.get_factors(n)
		fac_sum = 0
		for pair in factors:
			if n in pair:
				fac_sum += 1
			else:
				fac_sum += pair[0]
				if pair[0] != pair[1]:
					fac_sum += pair[1]
		memo_a[n] = fac_sum > n
	return memo_a[n]

def can_sum(n):
	for i in xrange(1, (n/2)+1):
		if is_abundant(i) and is_abundant(n-i):
			return True
	return False

running_sum = 0

for i in xrange(0, 28124):
	if not can_sum(i):
		running_sum += i
		print i


print(running_sum)
