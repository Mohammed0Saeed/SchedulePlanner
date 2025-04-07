class Course:
    def __init__(self, name, weekdays):
        self._name = name
        self._weekdays = weekdays

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def weekdays(self):
        return self._weekdays

    @weekdays.setter
    def weekdays(self, new_weekdays):
        self._weekdays = new_weekdays

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
