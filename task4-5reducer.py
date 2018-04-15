#!/usr/bin/python

"""task4-5reducer.py: Receives key, value pairs (pair of subsequent words, number of occurences), counts total number of occurences per pair of subsequent words"""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

prev_pair = ""
value_total = 0
pair = ""

for line in sys.stdin:		# for every line in the input
	line = line.strip()	# remove trailing characters
	if line:
		pair, value = line.split("\t", 1)	# get pair of words and it's occurences
		value = int(value)			
	
		# if is not the first occurence of the pair, increment value
		if prev_pair == pair:
			value_total += value
		else:	
			if prev_pair:
				print("{0}\t{1}".format(prev_pair, value_total))	# print pair + total occurences

			# set next pair's data
			value_total = value	
			prev_pair = pair

if prev_pair == pair: 		# don't forget the last key/value pair
	print("{0}\t{1}".format(prev_pair, value_total))
