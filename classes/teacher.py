class Teacher:
    def __init__(self, name, subjects, history):
        self._name = name
        self._subjects = subjects
        self._history = history

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

    def add_to_history(self, course, block, subject):
        self._history.append(f"{course}:{block}:{subject}")

    def __str__(self):
        return f"{self.name} teaches: ({self.subjects})"
