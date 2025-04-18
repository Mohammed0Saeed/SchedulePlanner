import csv

from classes import util

courses = util.load_courses("courses.csv")
teachers = util.load_teachers("teachers.csv")

pln = courses[1].create_course_plan()

print(pln)
