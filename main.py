import csv

from classes import util, plan, course, subject

courses = util.load_courses("courses.csv")
teachers = util.load_teachers("teachers.csv")

for c in courses:
    print(c)

for t in teachers:
    print(t)
