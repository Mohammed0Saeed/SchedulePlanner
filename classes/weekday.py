from classes import block

class Weekday:
    def __init__(self, name, blocks):
        self._name = name
        self._blocks = blocks

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, new_blocks):
        self._blocks = new_blocks

    """
    Adds a block to the weekday
    @:param block: the block to add
    """
    def add_block(self, block):
        self._blocks.append(block)

    """
    Removes a block from the weekday
    @:param block: the block to remove
    """
    def remove_block(self, block):
        self._blocks.remove(block)

    """
    Finds the first free block and fill it
    """
    def find_free_block(self):
        for b in self.blocks:
            if b.is_free():
                return b

        return None

    """
    Create a new weekday with four blocks
    """
    def create_empty_blocks(self):
        for i in range(0, 3):
            self._blocks += f",{block.Block(i, "#", "#")}"

    """
    Checks if the weekday is full
    @:return True: if the day is full
    """
    def is_full(self):
        for b in self.blocks:
            if b.is_free():
                return False

        return True

    """
    Fills the first available block in the day
    :param subject: the chosen subject
    :param teacher: the chosen teacher
    :return: None
    """
    def fill_first_block(self, subject, teacher):
        if self.is_full():
            raise Exception(f"{self._name} has no free blocks")

        for b in self.blocks:
            if b.is_free():
                b.subject = subject
                b.teacher = teacher
                break

    def __str__(self):
        return f"Weekday {self._name} has these blocks {self._blocks}"
