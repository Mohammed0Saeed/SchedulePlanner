# a program to set the number of available teachers for each subject
import signal
from lib import teacher, subjects, checkers
import csv, signal
from random import choice

def choose_teachers():
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

  with open("results/course_plan.csv","w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['course','subjects&teachers'])
    writer.writeheader()
    for row in plan:
      writer.writerow({'course' : row, 'subjects&teachers' : plan[row]})
    
    return plan
  
# get the teachers from the plan
def get_line(Arr):
  newArr = []
  for item in Arr:
    newArr.append(item.split(':')[1])
  return newArr

def check_repeat(Arr):
  for i in range(len(Arr)):
    c = 0
    for j in range(len(Arr)):
      if Arr[i] == Arr[j]:
        c += 1
      if c > 1:
        return False
  return True

def main():
  ...

if __name__ == "__main__":
  main()
