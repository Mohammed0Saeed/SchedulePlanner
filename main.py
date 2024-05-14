import csv
from lib import teacher
from lib import course
from lib import subjects
from random import randint

# getting all the data of a course
selectedCourse = course.read("dataBase/courses.csv", input("Course: "))

# create a random plan for the course
course.createRandomPlan(selectedCourse, selectedCourse['name'])