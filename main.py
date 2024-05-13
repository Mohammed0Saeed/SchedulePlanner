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
  i = 0 # counter for the blocks
  j = 0 # counter for the days
  c = 0 # counter through the days array
  while True:
    while True:
      # set j to the first chosen day
      j = randDays[c] - 1
      #check if the chosen place is free
      if plan[j][i] == "-":
        plan[j][i] = sub
        # take one from the class count to indicate that the class is given in the table
        classCount -= 1
        break
      else:
        # if the place is full, take the next place
        i += 1

      # if we are out of the index, chosen another day and chose another day
      if i > 3:
        if randDays[c] < 4: randDays[c] += 1
        else: randDays[c] = 0
        i = 0
      if classCount == 0:
        break
    
    i = 0
    c += 1
    if classCount == 0:
        break
    
with open(f"results/{selectedCourse['name']}_plan.csv", "w", newline='') as newPlan:
  writer = csv.DictWriter(newPlan, fieldnames=['days','Block1', 'Block2', 'Block3', 'Block4'])
  writer.writeheader()
  days = ['Mo', 'Di', 'Mi', 'Do', 'Fr']
  i = 0
  for row in plan:
    writer.writerow(
      {"days": days[i],
      "Block1" : row[0],
      "Block2" : row[1],
      "Block3" : row[2],
      "Block4" : row[3]}
    )
    i += 1