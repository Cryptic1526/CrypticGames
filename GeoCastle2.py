lockup = {
    "up the stairs": "keep",
    "description": "The Lockup is a dark and disgusting place. It's a long corridor lined with cells. The ground was cobble drenched in waste and mud, the inhabitants of this dreary place lay motionless, huddled into corners and quivering. Some squint at the light of the flaming torch and recoil. The way back though the corridor looks like a welcoming sight"
}

dungeon = {
    "up the stairs": "keep",
    "description": "You find yourself in a dimly lit dungeon. The walls are made of damp stones and the air is musty. A flight of stairs leads up to the keep. A dark torchlit corridor leads into the castle lockup."
}

house = {
    "through the door": "courtyard",
    "description": "You are in a house, made of mud bricks and cobblestones. The floor is dusty, and you can hear the sound of braying horses through the hole in the wall, a petty excuse for a window. A large oaken door lays closed in front of you"
}

courtyard = {
    "to the keep": "keep",
    "talk to the villager": "courtyard",
    "description": "The ground is muddy and unclean, and faint mist and smoke rises into the air from the open fires that bathe you in warmth. In the corner, there are some stone steps going up into your room, there is an archway leading down to the village below. Above you, on the hill, is the keep of the castle. A villager is loading potato sacks onto a horsedriven cart.",
    "item": "sword",
}

keep = {
    "inside": "inside",
    "down the stairs": "dungeon",
    "talk to the guard": "keep",
    "to the lockup": "lockup",
    "description": "The Keep is an open lawn, with barrels and carts going in and out of the arched gate. The village is visible below, the hill looming over the land like a beacon of light. A guard stands next to the big oakenfront doors leading inside. There is a dusty set of stairs leading down."
}
inside = {
    "description": "You are inside the keep. The sunlight shines through the stained windows, the ground is cobble with drapes of red carpet layed upon it. There are four doors. Two, plain spruce with iron edging on either side of a double-door embroidered with iron and silver.",
}

rooms = {
    "house": house,
    "courtyard": courtyard,
    "keep": keep,
    "dungeon": dungeon,
    "inside": inside,
    "lockup": lockup
}

#pls just work
previous_room = None
room = house

inventory = []
history = []

while True:
    print(room["description"])
    print("Inventory: ", inventory)

    move = input("What do you want to do? ")
    action = move.split()[0]

    if action == "go":
        
        direction = move.split(" ", 1)[1]    

        if direction in room:
            previous_room = room
            history.append(room)
            print("You have gone " + room[direction])
            room = rooms[ room[direction] ]
        else:
            print("You can't go that way!")
            
    elif action == "take":

        item = move.split(" ", 1)[1]
    
        print("You take the " + item)
        inventory.append(item)
    elif action == "talk":
        print("'Hello my lord! It's great to see you! You might want to go to the Guard Tower to start your first shift as a guard!'")

    elif action == "back":
        if previous_room:
            print("You go back to the " + previous_room)
            room, previous_room = previous_room, None
            room = history.pop()
        else:
            print("You can't go back any further!")
