#!/usr/bin/python

"""task7reducer.py: Receives values of matrix as column, row, value. Outputs matrix transpose."""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys
import operator

rowvalues = {}	# stores new row
rowstr = ""
prev_column = None

for line in sys.stdin:		# for every line in the input
	line = line.strip()	# remove trailing characters
	if line:
		column, row, value = line.split("\t")	# get column, row, value 
		column = int(column)
		row = int(row)
		if prev_column == column:		# if belongs to the same column
			rowvalues[row] = value		# append to new row
		else:
			if prev_column != None: 
				# sort by row index values
				sorted_rowvalues = dict(sorted(rowvalues.items(), key=operator.itemgetter(0)))
				rowstr = str(prev_column)+"\t"
				for i in sorted_rowvalues.values():	# create output
					rowstr += i+" "	
				print(rowstr)

			# reset values for next column
			prev_column = column		
			rowvalues = {}
			rowstr = ""
			rowvalues[row] = value

if prev_column == column: 		# don't forget the last key/value pair
	if len(rowvalues) > 0:
		# sort by row index values
		sorted_rowvalues = dict(sorted(rowvalues.items(), key=operator.itemgetter(0)))
		rowstr = str(prev_column)+"\t"
		for i in sorted_rowvalues.values():	# create output
			rowstr += i+" "	
		print(rowstr)
