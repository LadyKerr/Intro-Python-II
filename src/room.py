class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
#method to get player's next direction
    def get_direction(self, command):
        if command == "n":
            return self.n_to
        elif command == "s":
            return self.s_to
        elif command == "e":
            return self.e_to
        elif command == "w":
            return self.w_to
        else:
            return None
