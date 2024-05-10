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

# get the number of blocks from subjects.csv
classCount = int(subjects.read("dataBase/subjects.csv", 'DEU')['count']) + 1
randDays = []

# choose random days for the subject
for i in range(round(classCount / 2) + 1):
  day = randint(1, 5)
  if day not in randDays:
    randDays.append(day)

# fill the plan with the chosen subject
i = 0
while classCount != 0:
  for j in range(0, len(randDays)):
    plan[randDays[j] - 1][i] = 'DEU'
    classCount -= 1
    if classCount == 0:
      break
  i += 1

for row in plan:
  print(row)