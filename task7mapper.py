#!/usr/bin/python

"""task7mapper.py: Maps lines matrix lines as column, row, value """

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

for line in sys.stdin:				# input from standard input
	line = line.strip()			# remove whitespaces
	if line:
		column = 0			
		row, elements = line.split("\t")	# get row and it's values
		row_values = elements.split()		# split row values
		for value in row_values:
			print("{0}\t{1}\t{2}".format(column,row,value))	# print each value as column, row, value
			column += 1
		

