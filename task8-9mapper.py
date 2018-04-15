#!/usr/bin/python

"""task8mapper.py: Maps lines stundent's personal information as student_id, data_type, student_name for students and students' mark information as student_id, data_type, course, marks. """

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

for line in sys.stdin:				# input from standard input
	line = line.strip()			# remove whitespaces
	if line:
		data = line.split()		# get data
		if data[0] == "mark":
			print("{0}\t{1}\t{2}\t{3}".format(data[2],data[0],data[1],data[3]))
		elif data[0] == "student":
			print("{0}\t{1}\t{2}".format(data[1],data[0],data[2]))
		

