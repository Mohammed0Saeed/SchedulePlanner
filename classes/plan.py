import csv
from classes import util


class Plan:
    def __init__(self, name, courses):
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses

    @name.setter
    def name(self, new_name):
        self._name = new_name

    """
    add a course to the plan
    @:param course: course to add
    """
    def add_course(self, course):
        self._courses.append(course)

    """
    remove a course from the plan
    @:param course: course to remove
    """
    def remove_course(self, course):
        self._courses.remove(course)

    """
    Creates a plan for the given courses
    """
    def create_plan(self):
        self._courses = util.load_courses("courses.csv")
        for c in self._courses:
            c.create_course_plan()

    """
    Prints the plan
    """
    def print_plan(self):
        for c in self._courses:
            c.print_course_plan()

    """
    Creates a csv file containing the plan
    """
    def export_plan(self, filename):
        with open(f"results/{filename}", "w") as planFile:
            dictWriter = csv.DictWriter(planFile, fieldnames=["DAY", "BLOCK1", "BLOCK2", "BLOCK3", "BLOCK4"])
            for c in self._courses:
                planFile.write(f"### {c.name} ###\n")
                dictWriter.writeheader()
                for day in c.weekdays:
                    dictWriter.writerow({
                        "DAY": day.name,
                        "BLOCK1": "#" if day.blocks[0].is_free() else day.blocks[0],
                        "BLOCK2": "#" if day.blocks[1].is_free() else day.blocks[1],
                        "BLOCK3": "#" if day.blocks[2].is_free() else day.blocks[2],
                        "BLOCK4": "#" if day.blocks[3].is_free() else day.blocks[3],
                    })


    def __str__(self):
        return f"{self._name} has the courses: {self._courses}"
