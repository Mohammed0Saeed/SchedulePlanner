
class Plan:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    @property
    def name(self):
        return self.name
    @property
    def courses(self):
        return self.courses

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @courses.setter
    def courses(self, new_courses):
        self._courses = new_courses

    """
    add a course to the plan
    @:param course: course to add
    """
    def add_course(self, course):
        self.courses.append(course)

    """
    remove a course from the plan
    @:param course: course to remove
    """
    def remove_course(self, course):
        self.courses.remove(course)

    def __str__(self):
        return f"{self.name} has the courses: {self.courses}"