class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"\n Item is: {self.name} and it is {self.description}. "
    
    def __repr__(self):
        return f"\n Item:({repr(self.name)}) Desc:({repr(self.description)}) "

