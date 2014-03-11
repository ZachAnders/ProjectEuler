#!/usr/bin/env pypy

from datetime import date, timedelta

SUNDAY = 7

start = date(1901, 1, 1)
delta = timedelta(1)
end = date(2000, 12, 31)
sunday_counter = 0

while start != end:
	if start.isoweekday() == SUNDAY and start.day == 1:
		sunday_counter += 1
	start += delta

print(sunday_counter)
