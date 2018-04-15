#!/usr/bin/python

"""task1-2-3mapper.py: Maps lowercase lines."""

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

for line in sys.stdin:				# input from standard input
	line = line.strip()			# remove whitespaces
	if line:
		lower_case = line.lower()		# lower case line
		print lower_case
