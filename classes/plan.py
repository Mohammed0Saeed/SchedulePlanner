
class Plan:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    @getter
    def getName(self):
        return self.name
    @getter
    def getCourses(self):
        return self.courses

    @setter
    def setName(self, name):
        self.name = name

    @setter
    def setCourses(self, courses):
        self.courses = courses

    """
    add a course to the plan
    @:param course: course to add
    """
    def addCourse(self, course):
        self.courses.append(course)

    """
    remove a course from the plan
    @:param course: course to remove
    """
    def removeCourse(self, course):
        self.courses.remove(course)

    def __str__(self):
        print(self.name, "has the courses: ", self.courses)