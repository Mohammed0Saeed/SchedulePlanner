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
  for t in _teachers:
    if s in t['subjects'].split(','):
      tmpList.append(t['name'])
  print(f"Available Teachers for ({s}): {tmpList}")

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
      if randTeacher not in avTeacher:
        avTeacher[s] = randTeacher
        break

print(f"selected teachers: {avTeacher}")
