#!/usr/bin/env pypy

def charscore(achar):
	return ord(achar) - 64

total_score = 0

with open("data/22.txt", 'r') as names:
	line = names.readline()
	line = line.split(",")
	line = [name[1:-1] for name in line]
	line.sort()
	for name_pos in xrange(0, len(line)):
		name = line[name_pos]
		score = sum([charscore(each_char) for each_char in name])
		score *= (name_pos+1)
		total_score += score
		print("%s : %d" % (name, score))

#print(line)
print(total_score)
