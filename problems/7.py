#!/usr/bin/env pypy

from factor import get_factors

primes_found = 0
prime_to_get = 10001
current_prime = 1

while primes_found < prime_to_get-2:
	current_prime += 1
	if len(get_factors(current_prime)) == 1:
		primes_found += 1

print(current_prime)
