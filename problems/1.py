#!/usr/bin/env pypy

vals =[x for x in xrange(0,1000) if not (x%3) or not (x%5)]

print sum(vals)
