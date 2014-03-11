#!/usr/bin/env pypy

# Spelled twelve wrong, spent like 20 minutes trying to figure out the problem.
# Kind of disliked this problem because there were a couple frustrating issues like that :(
ones = {0: 'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
		10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

tens = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred', 1000:'one thousand'}

vals = {}

vals.update(ones)
vals.update(tens)
for base in xrange(10, 1000):
	if base not in vals:
		val = base
		outs = ""
		ones = val%10
		val /= 10
		tens = val%10
		val /= 10
		hundreds = val%10
		if hundreds != 0:
			if hundreds == 1:
				outs += "one hundred"
			else:
				outs += vals[hundreds] + " hundred"
			if tens != 0 or ones != 0:
				outs += " and "
		if tens > 1:
			outs += vals[tens*10]
			if ones != 0:
				outs += " "
				outs += vals[ones]
		else:
			if tens == 1:
				outs += vals[(tens*10)+ones]
			elif ones > 0:
				outs += vals[ones]
		vals[base] = outs

#print([val.replace(" ", '') for val in vals.values()])
for i in xrange(1, 1001):
	print(vals[i], len(vals[i].replace(' ', '')))
print(sum([len(vals[i].replace(" ", '')) for i in xrange(1, 1001)]))
