#!/usr/bin/env pypy

bound = 101

sqsum = sum([i**2 for i in xrange(0, bound)])
sumsq = sum([i for i in xrange(0, bound)])**2

print(sumsq - sqsum)
