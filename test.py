# a program to set the number of available teachers for each subject
from lib import teacher, subjects

teachers = teacher.readAll("dataBase/teachers.csv")
subject = subjects.readAll("dataBase/specSubject.csv")

orderedSubjects = {}

for s in subject:
  orderedSubjects[s['name']] = s['available']

sorted_dict = dict(sorted(orderedSubjects.items(), key=lambda x:x[1]))
print(sorted_dict)