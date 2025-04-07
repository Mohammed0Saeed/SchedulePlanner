class Teacher:
    def __init__(self, name, courses, history):
        self._name = name
        self._courses = courses
        self._history = history

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses

    @property
    def history(self):
        return self._history

    @name.setter
    def name(self, name):
        self._name = name

    @courses.setter
    def courses(self, courses):
        self._courses = courses

    @history.setter
    def history(self, history):
        self._history = history

    def add_to_history(self, course, block, subject):
        self._history.append(f"{course}:{block}:{subject}")
