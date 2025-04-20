from classes import util, weekday
from mesonbuild.mlog import exception
import csv


class Course:
    def __init__(self, name, subjects, weekly_count, weekdays):
        self._name = name
        self._subjects = subjects
        self._weekly_count = weekly_count
        self._weekdays = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, new_subjects):
        self._subjects = new_subjects

    @property
    def weekly_count(self):
        return self._weekly_count

    @weekly_count.setter
    def weekly_count(self, new_weekly_count):
        self._weekly_count = new_weekly_count

    @property
    def weekdays(self):
        return self._weekdays

    """
    Adds a subject in the csv file of the course
    @:param subject: the subject to be added
    """
    def add_subject(self, subject):
        # import all the data
        courses = []
        with open("courses.csv") as csv_file:
            for row in csv.reader(csv_file):
                courses.append(row.split(","))

        # add the subject to the list of subjects
        for c in courses:
            if c[0] == self.name:
                c[1] = c[1] + f";{subject}"
                break

            return exception("Error! course not found")

        # export the data to the csv file
        with open("courses.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(courses)

    """
    Adds a certain weekday to a course
    @:param weekday: the weekday to be added
    """
    def add_weekday(self, weekday):
        self._weekdays.append(weekday)

    """
    Removes a certain weekday from a course
    @:param weekday: the weekday to be removed
    """
    def remove_weekday(self, weekday):
        self._weekdays.remove(weekday)

    """
    Creates a plan for a week for the course
    """
    def create_course_plan(self):
        # choose the teachers
        chosen_teachers = util.choose_teachers(self)

        # create the weekdays
        days = ["MON", "TUE", "WED", "THU", "FRI"]
        week = []
        for day in days:
            week.append(weekday.Weekday(day, ""))

        # create blocks to fill
        for day in week:
            day.create_empty_blocks()

        # put each subject in its block
        for s in chosen_teachers:
            rand_days = util.choose_days_randomly(util.get_subject_count(s), week)
            for day in rand_days:
                day.fill_first_block(s, chosen_teachers[s], self._name)

        # add the filled days in the plan
        for day in week:
            self.add_weekday(day)

    """
    Print the plan in the console
    """
    def print_course_plan(self):
        print(f"### {self._name} ###")
        for day in self.weekdays:
            for b in day.blocks:
                if b.is_free():
                   print("empty | ", end="")
                else:
                    print(f"{b.subject}:{b.teacher.name} | ", end="")
            print()


    def __str__(self):
        return f"the course is: {self._name} and has {self._weekly_count} blocks a week"
