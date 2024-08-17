import csv
import os
import test
from lib import teacher, course, subjects, checkers
from random import randint, choice

def main():
  # clear the csv file before using 
  try:
    os.remove("results/plan.csv")
  except:
    pass
  # clear the history of teachers
  teacher.clear_history()

  # get the chosen teachers
  for i in range(1000):
    c = 0
    chosenTeachers = teacher.choose_teachers()
    for row in chosenTeachers:
      if teacher.is_repeated(chosenTeachers[row].split(',')) == False:
        c += 1
    if c < 1:
      for row in chosenTeachers:
        print(row, teacher.is_repeated(chosenTeachers[row].split(',')), chosenTeachers[row])
      print(i + 1, "very good version", c)
      break

  # getting all the data of a course
  selectedCourse = course.get_coursesNames()
  bigPlan = {}
  for _course in selectedCourse:
    while True:
      plan = course.new_createRandomCourse(course.read("dataBase/courses.csv", _course), chosenTeachers[_course])
      if checkers.checkPlan(plan):
        print(_course, "accepted")
        bigPlan[_course] = plan
        break
      else:
        print(_course, "not accepted")

  for items in bigPlan:
    with open(f"results/plan.csv", "a", newline='') as newPlan:
      writer = csv.DictWriter(newPlan, fieldnames=['days','Block1', 'Block2', 'Block3', 'Block4'])
      days = ['Mo', 'Di', 'Mi', 'Do', 'Fr']
      i = 0
      writer.writerow(
          {"days" : items,
          "Block1" : "---",
          "Block2" : "---",
          "Block3" : "---",
          "Block4" : "---"}
        )
      writer.writeheader()
      for row in bigPlan[items]:
        writer.writerow(
          {"days": days[i],
          "Block1" : row[0],
          "Block2" : row[1],
          "Block3" : row[2],
          "Block4" : row[3]}
        )
        i += 1
if __name__ == "__main__":
  main()