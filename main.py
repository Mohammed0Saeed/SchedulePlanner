import csv
import os
from lib import teacher, course, subjects, checkers
from random import randint

def main():
  # clear the csv file before using 
  os.remove("results/plan.csv")
  # getting all the data of a course
  while True:
    selectedCourse = course.get_coursesNames()
    bigPlan = []
    for _course in selectedCourse:
      while True:
        plan = createRandomCourse(course.read("dataBase/courses.csv", _course))
        if checkers.checkPlan(plan):
          bigPlan.append(plan)
          break
    if checkers.isOnlyOne(bigPlan) == False:
      break
  
  for j in range(len(bigPlan)):
    with open(f"results/plan.csv", "a", newline='') as newPlan:
      writer = csv.DictWriter(newPlan, fieldnames=['days','Block1', 'Block2', 'Block3', 'Block4'])
      days = ['Mo', 'Di', 'Mi', 'Do', 'Fr']
      i = 0
      writer.writerow(
          {"days" : selectedCourse[j],
          "Block1" : "---",
          "Block2" : "---",
          "Block3" : "---",
          "Block4" : "---"}
        )
      writer.writeheader()
      for row in bigPlan[j]:
        writer.writerow(
          {"days": days[i],
          "Block1" : row[0],
          "Block2" : row[1],
          "Block3" : row[2],
          "Block4" : row[3]}
        )
        i += 1
  print()

# check if no teacher have two classes at the same time

# a trail to see if this code would work
def chooseRandomTeachers(course):
    data = teacher.readAll("dataBase/teachers.csv")[1:]
    courseSubjects = subjects.sort(course['subjects'].split(','))
    #print(courseSubjects)
    chosen = {}
    for subj in courseSubjects:
      tmpList = []
      for te in data:
        if subj in te['subjects'].split(','):
          tmpList.append(te['name'])
      while True:
        randTeacher = tmpList[randint(0, (len(tmpList) - 1))]
        if randTeacher not in chosen:
          chosen[subj] = randTeacher
          break

    return chosen 

# create a random course and return an array
def createRandomCourse(selectedCourse):
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
  # use dictionary to store the data you need for the application
  history = {}

  for sub in selectedCourse['subjects'].split(','):
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

    chosenTeachers = chooseRandomTeachers(selectedCourse)
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
          plan[j][i] = f"{sub}:{chosenTeachers[sub]}"
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
    teacher.autoEdit("dataBase/teachers.csv", chosenTeachers[sub], "history", history)
    
  return plan

main()