import csv
import sys

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
