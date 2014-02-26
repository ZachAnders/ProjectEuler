#!/usr/bin/env pypy

def is_palin(aStr):
	tmp = list(aStr)
	tmp.reverse()
	return list(aStr) == tmp

palins = []
for i in xrange(100, 999):
	for j in xrange(100, 999):
		prod = i*j
		if is_palin(str(prod)):
			palins.append(prod)

print(max(palins))

