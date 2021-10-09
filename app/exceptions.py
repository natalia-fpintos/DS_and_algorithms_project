class StructureIsFullError(Exception):
    """Raised when attempting to add items to a data structure that is full"""
    def __init__(self, structure):
        self.structure = structure
        self.message = f'The {structure} is full, cannot add any more items'

