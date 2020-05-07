class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def change_location(self, new_location):
        self.new_location = new_location
