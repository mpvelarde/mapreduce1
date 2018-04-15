#!/usr/bin/python

"""task6reducer.py: Receives key, value pairs (pair of subsequent words, number of occurences), counts total number of occurences per pair of subsequent words"""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys
import operator

n = 20	# sets the amount of top most used pairs to store
# creates dictionary to store top n
pairs_dict = {}
pair = ""

for line in sys.stdin:		# for every line in the input
	line = line.strip()	# remove trailing characters
	if line:
		pair, value = line.split("\t", 1)	# get pair of words and it's occurences
		value = int(value)
	
		# if dictionary's size < n, append pair of words with its number of occurences as key
		if len(pairs_dict) < n:
			pairs_dict[pair] = value
		else:
			# get pair with less occurences
			k = min(pairs_dict, key=pairs_dict.get)
			# if pair's value is larger than min value
			if value > pairs_dict[k]:
				del pairs_dict[k]	# remove min value
				pairs_dict[pair] = value	# add new value
			


# sort dictionary desc
sorted_pairs_dict = dict(sorted(pairs_dict.items(), key=operator.itemgetter(1), reverse = True))

for i in sorted_pairs_dict:
	print("{0}".format(i))
