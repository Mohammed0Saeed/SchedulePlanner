import csv
from lib import teacher
from lib import course
from lib import subjects
from random import randint
_courses = course.readAll("dataBase/courses.csv")
_subjects = subjects.readAll("dataBase/subjects.csv")
_teachers = teacher.readAll("dataBase/teachers.csv")

# getting all the data of a course
selectedCourse = input("Course: ")

for row in _courses:
  if selectedCourse == row['name']:
    selectedCourse = row
    break

print(f"Required Subjects: {selectedCourse['subjects'].split(',')}")

# show the availabe teachers
avTeacher = {}
for s in selectedCourse['subjects'].split(','):
  tmpList = []
  teachersList = []
  for t in _teachers:
    if s in t['subjects'].split(','):
      tmpList.append(t['name'])

  if s == 'DEU':
    for i in range(2):
      randTeacher = tmpList[randint(0, (len(tmpList) - 1))]
      while True:
        if randTeacher not in avTeacher:
          avTeacher[s+str(i+1)] = randTeacher
          break
  else:
    while True:
      randTeacher = tmpList[randint(0, (len(tmpList) - 1))]
      if randTeacher not in teachersList:
        teachersList = randTeacher
        avTeacher[s] = randTeacher
        break

print(f"selected teachers: {avTeacher}")

# storing all informations related to the chosen teachers
teachersData = []
for k in avTeacher:
  teachersData.append(teacher.read("dataBase/teachers.csv", avTeacher[k]))

# creating 2d array to store the data in form of table
"""
the form of data is in this shape
    block1    block2    block3    block4
Mon   -         -         -         -
Tue   -         -         -         -
Wed   -         -         -         - 
Thu   -         -         -         -
Fri   -         -         -         -
"""
plan = [
  ['-', '-', '-', '-'],
  ['-', '-', '-', '-'],
  ['-', '-', '-', '-'],
  ['-', '-', '-', '-'],
  ['-', '-', '-', '-']
]

for sub in avTeacher:
  # get the number of blocks from subjects.csv
  classCount = int(subjects.read("dataBase/subjects.csv", sub)['count'])
  randDays = []

  # choose random days for the subject
  while True:
    day = randint(1, 5)
    if day not in randDays:
      randDays.append(day)

    if len(randDays) == classCount:
      break

  # fill the plan with the chosen subject
  i = 0 # blocks
  j = 0 # days
  c = 0 # iterator through the random days array
  overindex = False
  while True:
    while True:
      # set the j to one of the random days
      if overindex == False:
        j = randDays[c] - 1
      
      # check if the day is empty
      if plan[j][i] == "-":
        plan[j][i] = sub
        classCount -= 1
        # check that the value of c is not out of range 
        if c < len(randDays) - 1:
          c += 1
          i = 0
      else:
        if i < 3 and classCount != 0:
          i += 1
        elif i >= 3:
            overindex = True
            if 0 < j < 4:
              j += 1
            else:
              j = 0
        else:
          break
    if classCount == 0:
      break
    else:
      c = 0
      i = 0
    
    
for row in plan:
  print(row)