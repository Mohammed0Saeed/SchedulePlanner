class Teacher:
    def __init__(self, name, subjects, history):
        self._name = name
        self._subjects = subjects
        self._history = []

    @property
    def name(self):
        return self._name

    @property
    def subjects(self):
        return self._subjects

    @property
    def history(self):
        return self._history

    @name.setter
    def name(self, name):
        self._name = name

    @subjects.setter
    def subjects(self, subjects):
        self._subjects = subjects

    @history.setter
    def history(self, history):
        self._history = history

    """
    adds a course to the history of courses
    @:param course: course name
    """
    def add_to_history(self, course, block, subject):
        self._history.append(f"{course}:{block.index}:{subject}")

    """
    Returns the indices of the courses that the teacher has registered
    @:return indices: the indices of the courses that the teacher has registered
    """
    def get_indices(self):
        indices = []
        for data in self._history:
            indices.append(data.split(":")[1])
        return indices

    """
    Checks if the block is available for the teacher
    @:param block: the block to check
    @:return true: if the block is available for the teacher
    """
    def is_available(self, block):
        return block.index not in self.get_indices()

    """
    checks if a course has been already registered
    @:param course: course name
    @:return true: if course is in the history
    """
    def course_in_history(self, course):
        return course in self._history

    def __str__(self):
        return f"{self.name} teaches: ({self.subjects})"
