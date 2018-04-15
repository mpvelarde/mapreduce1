#!/usr/bin/python

"""task4-5-6mapper.py: Maps lines as key, value pair (pair of subsequent words in line, number of occurences)."""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

span = 2	# how many words we want to group (pairs -> 2)

for line in sys.stdin:				# input from standard input
	line = line.strip()			# remove whitespaces
	if line:
		words = line.split()			# split the line into tokens
		for i in range(0, len(words)):		# for all the words on the line
			if len(words[i:i+span]) > 1:	# if the word has a subsequent word
				subsequent_pair = " ".join(words[i:i+span]) 	# join the two subsequent words
				print("{0}\t{1}".format(subsequent_pair,1))	# print pair of words + occurences (1)

