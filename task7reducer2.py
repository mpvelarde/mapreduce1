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
		row, values = line.split("\t")	# get column, row, value 
		print values

