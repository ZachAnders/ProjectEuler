#!/usr/bin/env pypy

counter = 1 #$2 coin

target = 200

# pylint: disable=R0913
def get_val(p100=0, p50=0, p20=0, p10=0, p5=0, p2=0, p1=0):
	return 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + p1

for num100 in xrange(0, 3): #100p coin
	for num50 in xrange(0, ((200-get_val(num100))/50)+1):
		for num20 in xrange(0, ((200-get_val(num100, num50))/20)+1):
			for num10 in xrange(0, ((200-get_val(num100, num50, num20))/10)+1):
				for num5 in xrange(0, ((200-get_val(num100, num50, num20, num10))/5)+1):
					for num2 in xrange(0, ((200-get_val(num100, num50, num20, num10, num5))/2)+1):
						#num1 = 200 - get_val(num100, num50, num20, num10, num5, num2)
						counter += 1
						#outs = "%d\t"*7
						#print(outs % (num100, num50, num20, num10, num5, num2, num1))
print(counter)
