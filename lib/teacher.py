import csv
import sys
from random import randint, choice
from lib import subjects
# library for teacher file functions

# add a teacher to an existing list
def add(fileName):
    # store the teacher in form of classes
    class teacher:
        name = '',
        subjects = '',
        course = '',
        history = '',
        d_prefrence = '',
        t_prefrence = '',    

    teacher.name = input("Enter a name: ")
    teacher.subjects = input("Enter the subjects: ")
    teacher.course = input("Enter the letter of the course: ")
    teacher.history = "N/A"
    teacher.d_prefrence = input("Enter a day prefrence: ")
    teacher.t_prefrence = input("Enter a time prefrence (early/late): ")

    # append the new teacher to the list
    with open(fileName, "a", newline="") as teachersList:
        writer = csv.DictWriter(teachersList, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
        writer.writerow(
            {
                "name": teacher.name,
                "subjects": teacher.subjects,
                "course": teacher.course,
                "history": teacher.history,
                "d_prefrence": teacher.d_prefrence,
                "t_prefrence": teacher.t_prefrence
            })

# edit or delete an element
def edit(fileName, type):
    # load the file to this array
    fileList = []

    # add every row in the file to an array
    with open(fileName) as teacherList:
        reader = csv.DictReader(teacherList, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
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
                  case "course":
                      row['course'] = input("new courses: ")
                  case "history":
                      row['history'] = input("edit history: ")
                  case "d_prefrence":
                      row['d_prefrence'] = input("edit day prefrence: ")
                  case "t_prefrence":
                      row['t_prefrence'] = input("edit time prefrence: ")
                  case _:
                      raise ValueError
              break

      # upload the data to the file
      with open(fileName, "w", newline='') as teacherFile:
          writer = csv.DictWriter(teacherFile, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
          for row in fileList:
              writer.writerow({
                  'name': row['name'],
                  'subjects': row['subjects'],
                  'course': row['course'],
                  'history': row['history'],
                  'd_prefrence': row['d_prefrence'],
                  't_prefrence': row['t_prefrence']
              })

    elif type == "d":
      # upload the data to the file
      with open(fileName, "w", newline='') as teacherFile:
          writer = csv.DictWriter(teacherFile, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])

          # add all the elements except the deleted element
          for row in fileList:
              if row['name'] != key:
                  writer.writerow({
                  'name': row['name'],
                  'subjects': row['subjects'],
                  'course': row['course'],
                  'history': row['history'],
                  'd_prefrence': row['d_prefrence'],
                  't_prefrence': row['t_prefrence']
                })
    else:
        print(f"Invalid input for 'edit({fileName}, '{type}')'")

# auto editing for the history
def autoEdit(fileName, teacherName, data, change):
    # load the file to this array
    fileList = []

    # add every row in the file to an array
    with open(fileName) as teacherList:
        reader = csv.DictReader(teacherList, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
        for row in reader:
            fileList.append(row)

    # a key for the selected element
    key = teacherName

    # edit the data
    # check if the element in the list
    for row in fileList:
        if row['name'] == key:
            edit = data

            # edit the selected data of the chosen element
            match edit:
                case "name":
                    row['name'] = change
                case "subjects":
                    row['subjects'] = change
                case "course":
                    row['course'] = change
                case "history":
                    row["history"] = change
                case "d_prefrence":
                    row['d_prefrence'] = change
                case "t_prefrence":
                    row['t_prefrence'] = change
                case _:
                    raise ValueError
            break

    # upload the data to the file
    with open(fileName, "w", newline='') as teacherFile:
        writer = csv.DictWriter(teacherFile, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
        for row in fileList:
            writer.writerow({
                'name': row['name'],
                'subjects': row['subjects'],
                'course': row['course'],
                'history': row['history'],
                'd_prefrence': row['d_prefrence'],
                't_prefrence': row['t_prefrence']
            })

# read teacher's data
def read(fileName, teacher):
    with open(fileName) as cFile:
        reader = csv.DictReader(cFile, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
        for row in reader:
            if row['name'] == teacher:
                return row
        
        sys.exit("Not found!")

# read all the data from the dataBase
def readAll(fileName):
    dataBase = []
    with open(fileName) as cFile:
        reader = csv.DictReader(cFile, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
        for row in reader:
            dataBase.append(row)
    
    return dataBase

# get history from the teacher
def get_history():
    _teachers = {}
    for te in readAll("dataBase/teachers.csv"):
        _teachers[te['name']] = te['history']
    return _teachers

# clear the history before the execution
def clear_history():
    for te in readAll("dataBase/teachers.csv"):
        if te["history"] != "history":
            autoEdit("dataBase/teachers.csv", te['name'], "history", "")

# choose random teachers for a course
def chooseRandomTeachers(course):
  data = readAll("dataBase/teachers.csv")[1:]
  courseSubjects = subjects.sort(course['subjects'].split(','))
  #print(courseSubjects)
  chosen = {}
  for subj in courseSubjects:
    tmpList = []
    for te in data:
      if subj in te['subjects'].split(','):
        tmpList.append(te['name'])
    while True:
      randTeacher = choice(tmpList)
      # TODO this function misses accurecy
      if is_inDict(randTeacher, chosen) == False:
        chosen[subj] = randTeacher
        break

  return chosen 

# check if an element exists within the values
def is_inDict(element, dictionary):
    for item in dictionary:
        if element == dictionary[item]:
            return True
    return False

#
def is_full(teacher):
    classes = read("dataBase/teachers.csv", teacher)['history'].split("|")
    locations = []
    for item in classes:
        item = item.split(":")
        try:
            locations.append(f"{item[2]}:{item[3]}")
        except:
            pass
    return locations

# update history
def update_history(teacher, data):
    teachers = readAll("dataBase/teachers.csv")

    for te in teachers:
        if te['name'] == teacher:
            try:
                te['history'] += f",{data}"
            except:
                te['history'] = data
    
    with open("dataBase/teachers.csv", "w", newline='') as teacherFile:
        writer = csv.DictWriter(teacherFile, fieldnames=["name", "subjects", "course", "history", "d_prefrence", "t_prefrence"])
        for row in teachers:
            writer.writerow({
                'name': row['name'],
                'subjects': row['subjects'],
                'course': row['course'],
                'history': row['history'],
                'd_prefrence': row['d_prefrence'],
                't_prefrence': row['t_prefrence']
            })
# get all history information from a teacher
def get_teHistory(teacher):
    teachers = readAll("dataBase/teachers.csv")
    for te in teachers:
        if te['name'] == teacher:
            return te['history'].split("|")

# get the courses of a specific teacher
def get_courses(_teacher):
  courses = []
  for element in get_teHistory(_teacher):
    if element.split(":")[0] not in courses and element.split(":")[0] != "":
      courses.append(element.split(":")[0])
  return courses

# choose a random course
def choose(course):
    # show the availabe teachers
    avTeacher = {}
    for s in course['subjects'].split(','):
        tmpList = []
        teachersList = []
    for t in readAll("dataBase/teachers.csv"):
        if s in t['subjects'].split(','):
            tmpList.append(t['name'])
    
    while True:
        randTeacher = tmpList[randint(0, (len(tmpList) - 1))]
        if randTeacher not in teachersList:
            teachersList = randTeacher
            avTeacher[s] = randTeacher
            break
    
    return avTeacher