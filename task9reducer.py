#!/usr/bin/python

"""task9reducer.py: Receives stundents' personal information (student_id, data_type, student_name) and marks' information (student_id, data_type, course, marks). 
Gets min marks average by student, prints min average (or averages) """

__author__      = "Maria Velarde"
__copyright__   = "Amar es compartir"

import sys

prev_id = None
prev_type = None
marks = []
student = ""
avg = 0
mindata = {}	# stores the min averages (or averages)
minavg  = 100

for line in sys.stdin:		# for every line in the input
	line = line.strip()	# remove trailing characters
	if line:
		data = line.split("\t")	
		std_id = int(data[0])
		std_type = str(data[1])

		if prev_id == std_id:		# if belongs to the same student
			if std_type == "mark":	# append marks
				marks.append(data[3])
			elif std_type == "student":	# save name
				student = data[2]
		else:
			if len(marks) > 4:
				# get marks avg
				for i in marks:
					avg += float(i)
				avg = int(avg/float(len(marks)))

				if avg < minavg: # if smaller than current min
					minavg = avg	# update current min
					mindata = {}	# reset min data
					mindata[student] = avg
				elif avg == minavg:	# if equal than current min
					if not student in mindata:	# append the user to dict
						mindata[student] = avg	
			
			# set next students first line of info	
			avg = 0
			prev_id = std_id
			marks = []
			if std_type == "mark":
				marks.append(data[3])
			elif std_type == "student":
				student = data[2]

for i in mindata:	# print data
        print("{0}\t{1}".format(i, mindata[i]))
