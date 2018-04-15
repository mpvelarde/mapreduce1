#!/usr/bin/python

"""task3mapper2.py: Receives {0} {1}, where {0} is words total and {1} is lines total."""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

prev_sentence = ""
lines_total = 0
words_total = 0
sentence = ""

for line in sys.stdin:          		# for ever line in the input from stdin
	sentence = line.strip()         		# remove trailing characters
	if sentence:
		words, lines = sentence.split()		# get key value pair
		words_total += int(words)		# add num of words to total words
		lines_total += int(lines)		# add num of lines to total lines
		
print("{0} {1}".format(words_total, lines_total))	# print words_total lines_total
