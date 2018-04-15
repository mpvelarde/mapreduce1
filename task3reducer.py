#!/usr/bin/python

"""task3reducer.py: Receives lines, counts input's total lines and total words."""

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
		words = sentence.split()		# get words in line
		words_total += len(words)		# add num of words to total words
		lines_total = lines_total + 1		# add num of lines to total lines
		
print("{0} {1}".format(words_total, lines_total))	# print words_total lines_total



