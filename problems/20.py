#!/usr/bin/env pypy

import math

fact = math.factorial(100)

print(sum([int(i) for i in str(fact)]))
