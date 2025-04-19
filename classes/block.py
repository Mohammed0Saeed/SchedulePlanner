class Block:
    def __init__(self, index, teacher, subject):
        self._index = index
        self._teacher = teacher
        self._subject = subject

    @property
    def index(self):
        return self._index

    @property
    def teacher(self):
        return self._teacher

    @property
    def subject(self):
        return self._subject

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @teacher.setter
    def teacher(self, new_teacher):
        self._teacher = new_teacher

    @subject.setter
    def subject(self, new_subject):
        self._subject = new_subject

    """
    Checks if the block is free
    @:return True: if block is free
    """
    def is_free(self):
        return self._teacher == "#"

    def __str__(self):
        return f"{self._teacher.name}|{self._subject}"
