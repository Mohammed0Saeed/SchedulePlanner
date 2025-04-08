import csv

from mesonbuild.mlog import exception


class Course:
    def __init__(self, name, subjects, weekdays):
        self._name = name
        self._subjects = subjects
        self._weekdays = weekdays

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
    def weekdays(self):
        return self._weekdays

    @weekdays.setter
    def weekdays(self, new_weekdays):
        self._weekdays = new_weekdays

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

    def __str__(self):
        return f"the course is: {self._name}"
