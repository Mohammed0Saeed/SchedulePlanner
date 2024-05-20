import csv
import sys
# add a subject to the dataBase
def add(fileName):
    # store the subject in form of classes
    class subject:
        name = '',
        course = '',
        count = ''

    subject.name = input("Enter the name: ")
    subject.course = input("Enter the course: ")
    subject.count = int(input("Enter the number of the blocks: "))

    # append the new subject to the list
    with open(fileName, "a", newline='\n') as subjectList:
        writer = csv.DictWriter(subjectList, fieldnames=["name", "course", "count"])
        writer.writerow({"name": subject.name, "course": subject.course, "count": subject.count})

# edit or delete a data from the list
def edit(fileName, type):
    # load the file to this array
    fileList = []

    # add every row in the file to an array
    with open(fileName) as subjectList:
        reader = csv.DictReader(subjectList, fieldnames=["name", "course", "count"])
        for row in reader:
            fileList.append(row)

    # a key for the selected element
    key_subject = input("Key (subject): ")
    key_course = input("Key (course): ")

    # edit the data
    if type == 'e':
      # check if the element in the list
      for row in fileList:
          if row['name'] == key_subject:
              if row['course'] == key_course:
                  print("Element exists!")
              edit = input("Edit: ")

              # edit the selected data of the chosen element
              match edit:
                  case "name":
                      row['name'] = input("new name: ")
                  case "course":
                      row['course'] = input("new course: ")
                  case "count":
                      row['count'] = input("new count: ")
                  case _:
                      raise ValueError
              break

      # upload the data to the file
      with open(fileName, "w", newline='') as subjectFile:
          writer = csv.DictWriter(subjectFile, fieldnames=['name', 'course', 'count'])
          for row in fileList:
              writer.writerow({
                  'name': row['name'],
                  'course': row['course'],
                  'count': row['count']
              })

    elif type == "d":
      # upload the data to the file
      with open(fileName, "w", newline='') as subjectFile:
          writer = csv.DictWriter(subjectFile, fieldnames=['name', 'course', 'count'])

          # add all the elements except the deleted element
          for row in fileList:
              if row['name'] != key:
                  writer.writerow({
                  'name': row['name'],
                  'course': row['course'],
                  'count': row['count']
                })
    else:
        print(f"Invalid input for 'edit({fileName}, '{type}')'")
    
# read subject's data
def read(fileName, subject):
    with open(fileName) as cFile:
        reader = csv.DictReader(cFile, fieldnames=['name', 'course', 'count'])
        for row in reader:
            if row['name'] == subject:
                return row
        
        sys.exit("Not found!")

# read all the data from the dataBase
def readAll(fileName):
    dataBase = []
    with open(fileName) as cFile:
        reader = csv.DictReader(cFile, fieldnames=['name', 'course', 'count'])
        for row in reader:
            dataBase.append(row)
    
    return dataBase

# sort the subjects according to their number of blocks
def sort(array):
    Dict = {}
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if int(read("dataBase/subjects.csv", array[j])['count']) > int(read("dataBase/subjects.csv", array[j + 1])['count']):
                array[j], array[j + 1] = array[j + 1], array[j]

    return array