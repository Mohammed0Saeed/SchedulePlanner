from lib import teacher, subjects, course

def main():
  courses = ['GF1', 'MF1', 'TF1', 'TF2', 'WF2', 'GA1', 'MA1', 'TA1', 'TA2', 'WA2']

  for item in courses:
    print(teacher.chooseRandomTeachers(course.read("dataBase/courses.csv", item)))


main()
