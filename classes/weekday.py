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

    def __str__(self):
        return f"Weekday {self._name} has these blocks {self._blocks}"
