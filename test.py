# a program to set the number of available teachers for each subject
from lib import teacher, subjects
import csv
from random import choice
teachers = teacher.readAll("dataBase/teachers.csv")
subject = subjects.readAll("dataBase/specSubject.csv")

# some lists that i need
plan = {}
max_rate_teacher = {}
orderedSubjects = {}
subject_course = {}

for s in subject:
  subject_course[s['name']] = s['course']

for t in teachers:
  max_rate_teacher[t['name']] = 0


for s in subject:
  orderedSubjects[s['name']] = s['available']

sorted_subjects = dict(sorted(orderedSubjects.items(), key=lambda x:x[1]))

for s in sorted_subjects:
  # go through the teachers and get the teachers of this subject
  for c in subject_course[s].split(','):
    tmpList = []
    for t in teachers:
        if s in t['subjects'].split(','):
          tmpList.append(t['name'])

    # choose one random teacher
    while True:
        if len(tmpList) != 0:
          rand_teacher = choice(tmpList)
        else:
          break

        if max_rate_teacher[rand_teacher] < 4:
          max_rate_teacher[rand_teacher] += 1

          try:
            plan[c] += f",{s}:{rand_teacher}"
          except:
            plan[c] = f"{s}:{rand_teacher}"
          break


for row in max_rate_teacher:
  print(row, max_rate_teacher[row])

with open("results/course_plan.csv","w", newline='') as file:
  writer = csv.DictWriter(file, fieldnames=['course','subjects&teachers'])
  writer.writeheader()
  for row in plan:
    writer.writerow({'course' : row, 'subjects&teachers' : plan[row]})
