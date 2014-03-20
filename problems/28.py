#!/usr/bin/env pypy

target_dim = 1001

arr = {}

def coord_gen(dim):
	current = [dim/2, dim/2]
	yield tuple(current)
	for side_len in xrange(1, (dim/2)+1):
		current[0] += 1
		yield tuple(current)
		for _ in xrange((2*side_len)-1):
			current[1] += 1
			yield tuple(current)

		for _ in xrange(2*side_len):
			current[0] -= 1
			yield tuple(current)

		for _ in xrange(2*side_len):
			current[1] -= 1
			yield tuple(current)

		for _ in xrange(2*side_len):
			current[0] += 1
			yield tuple(current)

running_sum = 0
counter = 1
for coord in coord_gen(target_dim):
	if coord[0] == coord[1] or coord[0]+coord[1] == target_dim-1:
		running_sum += counter
	counter += 1

print(running_sum)
