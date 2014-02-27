#!/usr/bin/env pypy

import sys

def is_triplet(a,b,c):
	return (a**2 + b**2) == (c**2)

for a in xrange(1, 1000):
	for b in xrange(1, 1000-a):
		if is_triplet(a, b, 1000-(a+b)):
			print(str(a), str(b), str(1000-(a+b)))
			sys.exit(0)

