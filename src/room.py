# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"\n Room's name is: {self.name} and it is {self.description}. "
    
    def __repr__(self):
        return f"\n Room:({repr(self.name)}) Desc:({repr(self.description)}) "