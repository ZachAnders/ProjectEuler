#!/usr/bin/env pypy

a,b,acc = 1,1, []

while b < 4000000:
	c = a+b
	a = b
	b = c
	if not a%2:
		acc.append(a)
if not b%2:
	acc.append(b)

print(sum(acc))
