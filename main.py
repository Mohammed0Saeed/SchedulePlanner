import csv

def edit(fileName, type):
    # load the file to this array
    fileList = []

    # add every row in the file to an array
    with open(fileName) as teacherList:
        reader = csv.DictReader(teacherList, fieldnames=["name", "subjects", "course", "history"])
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
                  case _:
                      raise ValueError
              break

      # upload the data to the file
      with open(fileName, "w", newline='') as teacherFile:
          writer = csv.DictWriter(teacherFile, fieldnames=['name', 'subjects', 'course', 'history'])
          for row in fileList:
              writer.writerow({
                  'name': row['name'],
                  'subjects': row['subjects'],
                  'course': row['course'],
                  'history': row['history']
              })

    elif type == "d":
      # upload the data to the file
      with open(fileName, "w", newline='') as teacherFile:
          writer = csv.DictWriter(teacherFile, fieldnames=['name', 'subjects', 'course', 'history'])

          # add all the elements except the deleted element
          for row in fileList:
              if row['name'] != key:
                  writer.writerow({
                  'name': row['name'],
                  'subjects': row['subjects'],
                  'course': row['course'],
                  'history': row['history']
                })
    else:
        print(f"Invalid input for 'edit({fileName}, '{type}')'")
              
        




type = input("type: ")
edit("teachers.csv", type)