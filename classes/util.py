import csv, random

from classes import course, subject, teacher

"""
load the courses to the RAM
@:param: fileName the csv file in the dataBase
@:return courses: the array of courses
"""
def load_courses(file_name):
    courses = []
    with open(f"dataBase/{file_name}") as inputFile:
        for row in csv.reader(inputFile):
            courses.append(course.Course(row[0], row[1].split(";"), row[2],"null"))

    return courses[1:]

"""
load the subjects to the RAM
@:param: fileName the csv file in the dataBase
@:return subjects: the array of subjects
"""
def load_subjects(file_name):
    subjects = []
    with open(f"dataBase/{file_name}") as inputFile:
        for row in csv.reader(inputFile):
            subjects.append(subject.Subject(row[0], row[1]))

    return subjects[1:]

"""
load the teachers to the RAM
@:param fileName: the csv file in the dataBase
@:return teachers: the array of teachers
"""
def load_teachers(file_name):
    teachers = []
    with open(f"dataBase/{file_name}") as inputFile:
        for row in csv.reader(inputFile):
            teachers.append(teacher.Teacher(row[0], row[1].split(";"), "null"))

    return teachers[1:]

"""
choose teachers for each course
@:param course: the course
@:return subject_teacher: dictionary with chosen teachers for each subject
"""
def choose_teachers(_course):
    # a dictionary to with subject as a key and teacher as a value
    subject_teacher = {}

    subjects = priority_subjects(_course.subjects)
    teachers = load_teachers("teachers.csv")

    for subject in subjects:
        for _teacher in teachers:
            if subject in _teacher.subjects and len(_teacher.history) < 2 and not _teacher.course_in_history(_course):
                subject_teacher[subject] = _teacher
                _teacher.add_to_history(_course)
                break

    return subject_teacher

"""
order the subjects based on the available teachers
@:param subjects: array of subjects
@:return available_teachers: sorted list of subjects based on available teachers
"""
def priority_subjects(subjects):
    teachers = load_teachers("teachers.csv")
    available_teachers = {}

    for s in subjects:
        available_teachers[s] = 0
        for t in teachers:
            if s in t.subjects:
                available_teachers[s] += 1

    return sorted(available_teachers, key=available_teachers.get)

"""
Chooses n days randomly
@:param n: number of chosen days
@:param days: list of days
@:return rand_days: list of chosen days
"""
def choose_days_randomly(n, days):
    rand_days = []
    for i in range(int(n)):
        choice = random.choice(days)
        if choice not in rand_days and not choice.is_full():
            rand_days.append(choice)

    return rand_days

"""
Get the weekly count of subject in a week
@:param _subject: the searched subject
@:return s.week_count: the count of the subject
"""
def get_subject_count(_subject):
    subjects = load_subjects("subjects.csv")

    for s in subjects:
        if s.name == _subject:
            return s.week_count

    raise Exception(f"{_subject} is not found in dataBase")