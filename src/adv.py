from room import Room #this is the file room.py
from player import Player
from item import Item

#declare all items
items = {
    Item("map", "your one true guide"),
    Item("broom", "to help you fly"),
    Item("carpet", "to show you the world"),
    Item("lamp", "to light your way"),
    Item("compass", "to tell your direction")
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
# create a function to move from one room to the next room
# ask a user for an inout to determine where they want to go
# if user doesnt select a room, enter a standard warning

#  will need a helper function somewhere for the movements then invoke the function to make the player move
# 
# Make a new player object that is currently in the 'outside' room.
player_1 = Player("danny", room["outside"])
#print(player_1)

while True:
    print(f"\n Hey {player_1.name}! Your current location is {player_1.current_room.name}\n {player_1.current_room.description}\n")
    print("=======================")

    direction = input("Enter a direction: ") #this will be the command in the method get_direction
    if direction == "q":
        print("Thanks for playing! Bye!")
        break
    if direction == "n" or direction == "s" or direction == "e" or direction == "w":
        new_room = player_1.current_room.get_direction(direction)
        #player_1.change_location(new_room)
        if new_room == None:
            print("Whoops! You cannot move in that direction. Try again.")
            print("===========")
        else:
            player_1.change_location(new_room)
    
    
#use a while loop - look up while loops
#
# * Prints the current room name
#
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

