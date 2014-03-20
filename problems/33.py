#!/usr/bin/env pypy

def bad_simplify(numer, denom):
	numer = str(numer)
	denom = str(denom)

	common = [num for num in numer if num in denom]

	if len(common) == 1 and common[0] != '0':
		return [term.replace(common[0], '') for term in (numer, denom)]
	else:
		return [None, None]
	
for a in xrange(1, 100):
	for b in xrange(a, 100):
		x, y = bad_simplify(a, b)
		if x and y and int(y) != 0:
			if float(a)/b == float(x)/float(y):
				print("%d/%d  ==  %s/%s" % (a, b, x, y))
			
