import csv
from classes import course, teacher

"""
load the courses to the RAM
@:param: fileName the csv file in the dataBase
@:return courses: the array of courses
"""
def load_courses(file_name):
    courses = []
    with open(f"dataBase/{file_name}") as inputFile:
        for row in csv.reader(inputFile):
            courses.append(course.Course(row[0], row[1].split(";"), "null"))

    return courses

"""
load the teachers to the RAM
@:param fileName: the csv file in the dataBase
@:return courses: the array of teachers
"""
def load_teachers(file_name):
    courses = []
    with open(f"dataBase/{file_name}") as inputFile:
        for row in csv.reader(inputFile):
            courses.append(teacher.Teacher(row[0], row[1].split(";"), "null"))

    return courses