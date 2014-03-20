#!/usr/bin/env pypy

pd_products = set()
digits = set([str(num) for num in range(1, 10)])
running_sum = 0

def is_pandigital(mcand, multi, mproduct):
	val = str(mcand) + str(multi) + str(mproduct)
	if len(val) != 9 or len(digits.intersection(val)) != 9:
		return False
	return True

for mcand in xrange(1000):
	for multi in xrange(5000):
		product = mcand*multi
		if is_pandigital(mcand, multi, product) and product not in pd_products:
			pd_products.add(product)
			running_sum += product
			print("%s * %s = %s" % (mcand, multi, product))

print(running_sum)
