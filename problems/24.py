#!/usr/bin/env pypy

import itertools

# Apparently python's default permutation engine operates in lexicographical order
lexiter = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in xrange(0, 1000000-1):
	lexiter.next()

print lexiter.next()
