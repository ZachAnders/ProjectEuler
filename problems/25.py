#!/usr/bin/env pypy

f1, f2 = 1, 1
counter = 2

while len(str(f2)) < 1000:
	f1, f2 = f2, f1+f2
	counter += 1
	#print counter, f2

print(counter, f2)
