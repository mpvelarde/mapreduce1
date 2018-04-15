#!/usr/bin/python

"""task7reducer.py: Receives values of matrix as column, row, value. Outputs matrix transpose."""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys
import operator

rowstr = ""
prev_column = None
prev_row = None

for line in sys.stdin:		# for every line in the input
	line = line.strip()	# remove trailing characters
	if line:
		column, row, value = line.split("\t")	# get column, row, value 
		column = int(column)
		row = int(row)
		if prev_column == column:		# if belongs to the same column
			sys.stdout.write(value+" ")
		else:
			# reset values for next column
			if prev_column !=None: sys.stdout.write("\n")
			prev_column = column		
			rowstr = ""
			sys.stdout.write(str(column)+"\t"+value+" ")

sys.stdout.write("\n")

