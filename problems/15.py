#!/usr/bin/env pypy

memo = {}
def descend(avail0s, avail1s):
	if avail0s == 0 or avail1s == 0:
		return 1
	key = (avail0s, avail1s)
	if (avail0s, avail1s) not in memo:
		memo[key] = descend(avail0s-1, avail1s) + descend(avail0s, avail1s-1)
	return memo[key]

for i in xrange(2, 21):
	print("%dx%d: %d" % (i, i, descend(i, i)))


