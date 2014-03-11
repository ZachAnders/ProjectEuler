#!/usr/bin/env pypy

base = 10**9000

def det_pattern(n):
	max_patt_len = 0
	max_patt_ratio = 0
	for pat_len in xrange(1, len(n)):
		substr = n[-pat_len:]
		val = n.count(substr)
		match_len = val*pat_len
		if float(match_len)/len(n) > .90 and val > 1:
			if n[-(match_len):].count(substr) == val:
				return pat_len
	return max_patt_len

max_val = (0, 0, 0)

for i in xrange(1, 1000):
	test_val = base/i
	test_len = det_pattern(str(test_val))
	if test_len > max_val[2]:
		max_val = (i, str(test_val), test_len)

#print(max_val)
print("Longest repeat: %d" % (max_val[0]))
