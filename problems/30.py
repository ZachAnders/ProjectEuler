#!/usr/bin/env pypy

exponent = 5
upper_bound = 10**6

def check_digits(val, exp):
	digit_sum = 0
	current_val = int(val)
	while current_val != 0:
		digit_sum += (current_val%10)**exp
		current_val /= 10
	return digit_sum == val

running_sum = 0
for current_test in xrange(2, upper_bound):
	if check_digits(current_test, exponent):
		running_sum += current_test

print(running_sum)
