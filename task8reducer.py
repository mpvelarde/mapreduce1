#!/usr/bin/python

"""task8reducer.py: Receives stundents' personal information (student_id, data_type, student_name) and marks' information (student_id, data_type, course, marks). 
Performs join by student id, outputs: student_name --> (course, marks), (course, marks),..... """

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

prev_id = None
prev_type = None
marks = []
student = ""

for line in sys.stdin:		# for every line in the input
	line = line.strip()	# remove trailing characters
	if line:
		data = line.split("\t")		# get data from stdin 
		std_id = int(data[0])
		std_type = str(data[1])

		if prev_id == std_id:		# if belongs to the same student
			if std_type == "mark":	# append marks
				marks.append("("+data[2]+", "+data[3]+")")
			elif std_type == "student":	# save name
				student = data[2]+" --> "
		else:
			for i in marks:	# create string for marks
				student += i+" "
			if len(marks) > 0:
				print student	# print
			
			# set next students first line of info
			prev_id = std_id
			marks = []
			if std_type == "mark":
				marks.append("("+data[2]+", "+data[3]+")")
			elif std_type == "student":
				student = ""+data[2]+" --> "

if prev_id == std_id:
	if prev_id:
		for i in marks:	# create string for marks
			student += i+" "
		if len(marks) > 0:
			print student	# print
