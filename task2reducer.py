#!/usr/bin/python

"""task2reducer.py: Receives lines as key value, outputs only first occurence of a line."""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

prev_sentence = ""
value_total = 0
sentence = ""

for line in sys.stdin:          		# for ever line in the input from stdin
	sentence = line.strip()         		# remove trailing characters
	if sentence:
		if prev_sentence != sentence:		# if line's first occurence
			if prev_sentence:  		# write result to stdout
				print(prev_sentence)
			prev_sentence = sentence

if prev_sentence == sentence: 		# don't forget the last sentence
	print(prev_sentence)



