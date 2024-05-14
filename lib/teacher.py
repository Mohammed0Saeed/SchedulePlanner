import csv
import sys
from random import randint
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