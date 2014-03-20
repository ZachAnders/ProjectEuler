#!/usr/bin/env pypy

vals = []
upper_bound = 101

for a in xrange(2, upper_bound):
	for b in xrange(2, upper_bound):
		current_val = a**b
		if current_val not in vals:
			vals.append(current_val)

print(len(vals))
