#!/usr/bin/env pypy

from factor import get_factors

counter = 1
accumulator = 0
max_factors = 0

while max_factors <= 250:
	accumulator += counter
	counter += 1
	factors = len(get_factors(accumulator))
	if factors > max_factors:
		max_factors = factors

print(accumulator)
