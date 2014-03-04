#!/usr/bin/env pypy

counter = 1 # Counts off starting nums
max_len = 0 # Maximum seen sequence length
max_start = 0 # Start value that caused maximum length
current_iter_num = 0 # Number of iterations
current_iter_val = 0 # Iterations result (i.e. 'n')

bound = 1000000

while counter < bound:
	current_iter_val = counter
	current_iter_num = 0
	while current_iter_val != 1:
		if current_iter_val % 2:
			current_iter_val = 3*current_iter_val + 1
		else:
			current_iter_val /= 2
		current_iter_num += 1
	if current_iter_num > max_len:
		max_len = current_iter_num
		max_start = counter
	if not counter%(bound/25):
		print(counter)
	counter += 1

print("Largest sequence found: Started at %d created sequence %d long." % (max_start, max_len))
print(max_start)
