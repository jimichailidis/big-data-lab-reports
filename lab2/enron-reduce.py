#!/usr/bin/env python
import sys
current_count = 0
current_word = ""
for line in sys.stdin:
	line = line.strip().split('\t')
	if len(line) != 1:
		continue

	key = line[0]
	if (key != current_word):
		if (current_count > 0):
			print str(current_count) + '\t' + current_word
			current_count = 0
		current_word = key
	current_count += 1

if (current_count > 0):
	# print current_word + '\t' + str(current_count)
	print str(current_count) + '\t' + current_word
