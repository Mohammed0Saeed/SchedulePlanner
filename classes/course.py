class Course:
    def __init__(self, name, weekdays):
        self.name = name
        self.weekdays = weekdays

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def weekdays(self):
        return self.weekdays

    @weekdays.setter
    def weekdays(self, new_weekdays):
        self.weekdays = new_weekdays

    """
    Adds a certain weekday from a course
    @:param weekday: the weekday to be added
    """
    def add_weekday(self, weekday):
        self.weekdays.append(weekday)

    """
    Removes a certain weekday from a course
    @:param weekday: the weekday to be removed
    """
    def remove_weekday(self, weekday):
        self.weekdays.remove(weekday)

    def __str__(self):
        return f"the course is: {self.name}"