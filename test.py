# TODO now try to choose the teachers first

from lib import teacher, course, subjects
import random

teachers_count = {}
teachers = []
courses = []
chosen_teachers = {}

# teachers getter
with open("dataBase/teachers.csv") as tFile:
  for row in tFile:
    row = row.split(",")
    if row[0] != "name":
      teachers_count[row[0]] = 0
      teachers.append(row[0])
  
# courses getter
with open("dataBase/courses.csv") as cFile:
  for row in cFile:
    row = row.split(",")
    if row[0] != "name":
      courses.append(row[0])

# choosing the course for each teacher
for c in courses:
  # get the data of the chosen course
  newC = course.read("dataBase/courses.csv", c)
  tmp_chosen = {}

  # run through each subject in that course
  for s in newC['subjects'].split(","):
    # a temporary list to get all the teachers of that specific subject
    tmp_list = []

    # get all the teachers of the chosen subject
    for t in teachers:
      if s in teacher.read('dataBase/teachers.csv', t)['subjects'].split(','):
        tmp_list.append(t)

    while True:
      rand_teacher = random.choice(tmp_list)

      if rand_teacher not in tmp_chosen and teachers_count[rand_teacher] <= 2:
        tmp_chosen[s] = rand_teacher
        teachers_count[rand_teacher] += 1
        print(c, s, rand_teacher, teachers_count[rand_teacher])
        break

  chosen_teachers[c] = tmp_chosen


for item in chosen_teachers:
  print(item, chosen_teachers[item])

for t in teachers_count:
  print(t, teachers_count[t])