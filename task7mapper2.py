#!/usr/bin/python

"""task7mapper2.py: Maps matrix lines as row value s """

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

for line in sys.stdin:				# input from standard input
	line = line.strip()			# remove whitespaces
	if line:			
		row, elements = line.split("\t")	# get row and it's values
		print("{0}\t{1}".format(row,elements))	# print each value as column, row, value
		

