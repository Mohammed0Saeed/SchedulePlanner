class Block:
    def __init__(self, teacher, subject):
        self.teacher = teacher
        self.subject = subject

    @property
    def teacher(self):
        return self.teacher

    @property
    def subject(self):
        return self.subject

    @teacher.setter
    def teacher(self, new_teacher):
        self.teacher = new_teacher

    @subject.setter
    def subject(self, new_subject):
        self.subject = new_subject

    def __str__(self):
        return f"{self.teacher}|{self.subject}"