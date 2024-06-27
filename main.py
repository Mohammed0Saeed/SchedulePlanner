import csv
import os
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
  # getting all the data of a course
  selectedCourse = course.get_coursesNames()
  bigPlan = {}
  _teachers = teacher.get_history()
  for _course in selectedCourse:
    while True:
      plan = course.createRandomCourse(course.read("dataBase/courses.csv", _course), _teachers)
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
  print()

main()