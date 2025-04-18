class Subject:
    def __init__(self, name, week_count):
        self._name = name
        self._week_count = week_count

    @property
    def name(self):
        return self._name

    @property
    def week_count(self):
        return self._week_count

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @week_count.setter
    def week_count(self, new_week_count):
        self._week_count = new_week_count

    def __str__(self):
        plural_form = "es" if self.week_count > 1 else ""
        return f"{self.name} has {self.week_count} class{plural_form} a week"
