import csv
from lib import teacher, course, subjects
from random import randint
from sys import exit

def main():
  # getting all the data of a course
  #selectedCourse = course.read("dataBase/courses.csv", input("Course: "))
    selectedCourse = course.read("dataBase/courses.csv", "TF2")
    for i in range(1):
      chooseRandomTeachers(selectedCourse)
  # for i in range(1):
  #   createRandomCourse(selectedCourse, ("TF2_" + str(i)))
  #   checkPlan(f"results/{selectedCourse['name']}_" + str(i) + "_plan.csv")

def checkPlan(fileName):
  with open(fileName) as cFile:
      reader = csv.DictReader(cFile, fieldnames=['days', 'block1', 'block2', 'block3', 'block4'])
      empty = 0

      for row in reader:
        if row['block4'] == "-":
          empty += 1
      
      if empty >= 3:
        print(fileName, "is good")

# a trail to see if this code would work
def chooseRandomTeachers(course):
  chosenTeacher = []
  _subjects = course['subjects'].split(',')
  for subject in _subjects:
    tmpList = []
    for t in teacher.readAll("dataBase/teachers.csv"):
      if subject in t['subjects'].split(','):
        tmpList.append(t['name'])
        while True:
          try:
            randChoice = tmpList[randint(0, len(tmpList) - 1)]
              
            if randChoice in chosenTeacher:
              continue
            else:
              chosenTeacher.append(t['name'])
              break
          except:
            exit(f"{subject} has a problem")

  # if len(chosenTeacher) != 7:
  #   print("WTF?")
  # else:
    print(tmpList, len(tmpList))
  print(chosenTeacher)

def createRandomCourse(selectedCourse, fileName):
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
      
  with open(f"results/{fileName}_plan.csv", "w", newline='') as newPlan:
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
# you should sort the teachers according to their prefrence
# you should add a function to update the history of a course
# a bug that must be solved
"""
Course: TF2
{'DEU1': 'VOR', 'GMT': 'KRZ', 'ANA': 'TAV', 'DEU2': 'OST', 'PHY': 'KEM', 'CHE': 'KRZ', 'INF': 'TAV'} 
"""

main()