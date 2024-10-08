import csv
import sys
from random import choice, randint
import test
from lib import subjects, teacher, course, checkers

# add a course to the list of courses
def add(fileName):
    # store the teacher in form of classes
    class course:
        name = '',
        subjects = '',
        blocks = '',
        history = ''

    course.name = input("Enter the name: ")
    course.subjects = input("Enter the subjects: ")
    course.blocks = int(input("Enter the number of the blocks: "))
    course.history = "N/A"

    # append the new teacher to the list
    with open(fileName, "a") as courseList:
        writer = csv.DictWriter(courseList, fieldnames=["name", "subjects", "blocks", "history"])
        writer.writerow(
            {"name": course.name, "subjects": course.subjects, "blocks": course.blocks, "history": course.history})

# edit or remove a course from the list
def edit(fileName, type):
    # load the file to this array
    fileList = []

    # add every row in the file to an array
    with open(fileName) as courseList:
        reader = csv.DictReader(courseList, fieldnames=["name", "subjects", "blocks", "history"])
        for row in reader:
            fileList.append(row)

    # a key for the selected element
    key = input("Key: ")

    # edit the data
    if type == 'e':
      # check if the element in the list
      for row in fileList:
          if row['name'] == key:
              print("Element exists!")
              edit = input("Edit: ")

              # edit the selected data of the chosen element
              match edit:
                  case "name":
                      row['name'] = input("new name: ")
                  case "subjects":
                      row['subjects'] = input("new subjects: ")
                  case "blocks":
                      row['blocks'] = input("new count of blocks: ")
                  case "history":
                      row['history'] = input("edit history: ")
                  case _:
                      raise ValueError
              break

      # upload the data to the file
      with open(fileName, "w", newline='') as courseList:
          writer = csv.DictWriter(courseList, fieldnames=['name', 'subjects', 'blocks', 'history'])
          for row in fileList:
              writer.writerow({
                  'name': row['name'],
                  'subjects': row['subjects'],
                  'blocks': row['blocks'],
                  'history': row['history']
              })

    elif type == "d":
      # upload the data to the file
      with open(fileName, "w", newline='') as courseFile:
          writer = csv.DictWriter(courseFile, fieldnames=['name', 'subjects', 'blocks', 'history'])

          # add all the elements except the deleted element
          for row in fileList:
              if row['name'] != key:
                  writer.writerow({
                  'name': row['name'],
                  'subjects': row['subjects'],
                  'blocks': row['blocks'],
                  'history': row['history']
                })
    else:
        print(f"Invalid input for 'edit({fileName}, '{type}')'")

# read a specific course data
def read(fileName, course):
    with open(fileName) as cFile:
        reader = csv.DictReader(cFile, fieldnames=["name", "subjects", "blocks", "history"])
        for row in reader:
            if row['name'] == course:
                return row
        
        sys.exit("Not found!")

# get all the data from the dataBase
def readAll(fileName):
    dataBase = []
    with open(fileName) as cFile:
        reader = csv.DictReader(cFile, fieldnames=['name', 'subjects', 'blocks', 'history'])
        for row in reader:
            dataBase.append(row)
    
    return dataBase

# get the name of the courses
def get_coursesNames():
    courses = readAll("dataBase/courses.csv")
    courseNames = []

    for course in courses:
        if course["name"] != "name":
            courseNames.append(course["name"])

    return courseNames

# remove an element from an array
def remove(arr, el):
  newArr = []
  for item in arr:
    if item != el:
      newArr.append(item)
  return newArr

def new_createRandomCourse(selectedCourse, chosen):
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

  # a counter for the checker of the plan
  bigPlanLen = 0
  # --- #
  # use dictionary to store the data you need for the application
  subs = selectedCourse['subjects'].split(',')

  chosenTeachers = {}
  for item in chosen.split(","):
     item = item.split(":")
     chosenTeachers[item[0]] = item[1]

  for randSub in subs:
    classCount = int(subjects.read("dataBase/subjects.csv", randSub)['count'])
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
        if j > 4:
           j -= 1
        #check if the chosen place is free
        #TODO make a better condition for the seletion and distribution
        #and f"{j}:{i}" not in teacher.is_full(chosenTeachers[randSub]):
        if plan[j][i] == "-":
          plan[j][i] = f"{randSub}:{chosenTeachers[randSub]}"
          # take one from the class count to indicate that the class is given in the table
          classCount -= 1
          break
        else:
          # if the place is full, take the next place
          i += 1

        # if we are out of the index, chosen another day and chose another day
        if i > 3:
          i = 0
          randDays[c] += 1
        if classCount == 0:
          break
      
      i = 0
      c += 1
      if classCount == 0:
          break
        
    #subs = remove(subs, randSub)
    bigPlanLen += 1

  return plan