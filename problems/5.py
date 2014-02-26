#!/usr/bin/python
import math

counter = 0
current_test = 1
while counter < 20:
	current_test += 1
	counter = 0
	for i in xrange(1, 21):
		if current_test%i:
			break
		counter += 1

print current_test
