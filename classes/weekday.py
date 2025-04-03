class Weekday:
    def __init__(self, name, blocks):
        self.name = name
        self.blocks = blocks

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def blocks(self):
        return self.blocks

    @blocks.setter
    def blocks(self, new_blocks):
        self.blocks = new_blocks

    """
    Adds a block to the weekday
    @:param block: the block to add
    """
    def add_block(self, block):
        self.blocks.append(block)

    """
    Removes a block to the weekday
    @:param block: the block to remove
    """
    def remove_block(self, block):
        self.blocks.remove(block)

    def __str__(self):
        return f"Weekday {self.name} has these blocks {self.blocks}"