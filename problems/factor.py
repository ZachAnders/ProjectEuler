#!/usr/bin/env pypy

import math, pickle, os, sys, gzip
test_ranges = [(2, 10000), (40000, 41000), (2000, 5000), (800000, 810000), (10000, 25000)]

def get_factors(val):
	factors = [(1, val)]
	if val < 4:
		return factors
	bound = int(math.sqrt(val)+1)
	for test_factor in xrange(2, bound):
		if val % test_factor == 0:
			factors.append((test_factor, val/test_factor))
	return factors

def get_fname(first_num, last_num):
	return "./test/factors_" + str(first_num) + "-" + str(last_num)

def save_factors(first_num, last_num):
	factors = factor_range(first_num, last_num)
	#with open(fname, "w") as save_file:
	with gzip.GzipFile(get_fname(first_num, last_num), "w", 9) as save_file:
		pickle.dump(factors, save_file)

def load_factors(first_num, last_num):
	fname = get_fname(first_num, last_num)
	if not os.path.exists(fname):
		return None

	with gzip.GzipFile(fname, "r") as load_file:
		return pickle.load(load_file)

def factor_range(first_num, last_num):
	return [get_factors(i) for i in xrange(first_num, last_num)]


if __name__ == "__main__":
	print("Running factor tests...")
	for (first, last) in test_ranges:
		print("Doing test: %d to %d" % (first, last))
		knowns = load_factors(first, last)
		if knowns == None:
			print("No knowns for range %d-%d. Recording baseline results." % (first, last))
			save_factors(first, last)
		else:
			calculated = factor_range(first, last)
			if knowns == calculated:
				print("Test passed. Numbers factored: %d" % (last-first))
			else:
				print("Test FAILED.")
				for each in xrange(first, last):
					if knowns[each] != calculated[each]:
						print("Differing factors for %d." % (each))
						print("Known: " + str(knowns[each]))
						print("Calculated: " + str(calculated[each]))
				print("Skipping remaining tests.")
				sys.exit(1)
