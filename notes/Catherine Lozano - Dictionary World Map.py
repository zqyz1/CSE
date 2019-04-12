world_map = {
    'ORPHANAGE': {
        'NAME': "Sam's Orphanage",
        'DESCRIPTION': "This is the room that you are in right "
                       "now. It has one exit. To the north is the hospital.",
        'PATHS': {
            'NORTH': "HOSPITAL"
        }
    },
    'HOSPITAL': {
        'NAME': "UCLA Medical Center",
        'DESCRIPTION': "This is were sick patients come in, you'll "
                       "have to pass by here to get to your destination."
                       "To the south is the meat warehouse.",
        'PATHS': {
            'SOUTH': "MEAT WAREHOUSE"
        }
    },
    'MEAT WAREHOUSE': {
        'NAME': "Butcher's Warehouse",
        'DESCRIPTION': "This is the most famous warehouse. To the south"
                       "is the school.",
        'PATHS': {
            'SOUTH': "SCHOOL"
        }
    },
    'SCHOOL': {
        'NAME': "Edison High School",
        'DESCRIPTION': "This is the school you attend. To the east is the wood shop.",
        'PATHS': {
            'EAST': "WOOD SHOP"
        }
    },
    'WOOD SHOP': {
        'NAME': "Sam's Wood Shop",
        'DESCRIPTION': "In this wood shop uou can grab a"
                       "hammer, to help you later on break "
                       "into the Chicken Noodle Soup Factory."
                       "To the south is the cemetery.",
        'PATHS': {
            'SOUTH': "CEMETERY"
        }
    },
    'CEMETERY': {
        'NAME': "Animal Cemetery Center",
        'DESCRIPTION': "This cemetery is hard to go through"
                       "because of you parents burying your dog"
                       "here. To the east is the box",
        'PATHS': {
            'EAST': "BOX"
        }
    },
    'BOX': {
        'NAME': "Catherine's Box",
        'DESCRIPTION': "This is where you live, you will go in the "
                       "box and grab a light, to help you along the way."
                       "To the south is the house.",
        'PATHS': {
            'SOUTH': "HOUSE"
        }
    },
    'HOUSE': {
        'NAME': "Delaney's House",
        'DESCRIPTION': "When you arrive to the house, you will have to "
                       "break in. It's an abandoned house, you will need "
                       "your flashlight to go through the house. To the west is the grocery store.",
        'PATHS': {
            'WEST': "GROCERY STORE"
        }
    },
    'GROCERY STORE': {
        'NAME': "Sam's Grocery Store",
        'DESCRIPTION': "Here you will find food, you will eat whatever "
                       "helps you from starving to death. To the south"
                       "is the secret door.",
        'PATHS': {
            'SOUTH': "SECRET DOOR"
        }
    },
    'SECRET DOOR': {
        'NAME': "Secret Door",
        'DESCRIPTION': "You have unlocked a secret room that leads you to"
                       "the apartments. You'll have to go west. ",
        'PATHS': {
            'WEST': "APARTMENT"
        }
    },
    'APARTMENT': {
        'NAME': "Sam's Apartment Village",
        'DESCRIPTION': "This is where you will be supplied with food,"
                       "you'll need energy, it's to the south. ",
        'PATHS': {
            'SOUTH': "SHELTER"
        }
    },
    'SHELTER': {
        'NAME': "Homeless Shelter",
        'DESCRIPTION': "In here you'll find wise homeless people,"
                       "they'll give you some advise on how to break into the factory."
                       "Afterwards, head south, to the police station. ",
        'PATHS': {
            'SOUTH': "POLICE STATION"
        }
    },
    'POLICE STATION': {
        'NAME': "Police Station",
        'DESCRIPTION': "This is where you'll have a talk with the inmates,"
                       "you'll learn of many different ways to break into a"
                       "place. The information will help you. To the south is the blueberry farm. ",
        'PATHS': {
            'SOUTH': "BLUEBERRY FARM"
        }
    },
    'BLUEBERRY FARM': {
        'NAME': "Sam's Blueberry Farm",
        'DESCRIPTION': "In order to get to the Chicken Noodle SOup Factory, \n you'll need to break into this farm. "
                       "It's the only way. To the south is the blueberry factory.",
        'PATHS': {
            'SOUTH': "BLUEBERRY FACTORY"
        }
    },
    'BLUEBERRY FACTORY': {
        'NAME': "Sam's Blueberry Factory",
        'DESCRIPTION': "You'll also have to break into the factory,"
                       "this break in will also prepare you for the "
                       "Chick++ Noodle Soup Factory break in. To the east is the blueberry factory.",
        'PATHS': {
            'EAST': "SOUP FACTORY"
        }
    },
    'SOUP FACTORY': {
        'NAME': "Chicken Noodle Soup Factory",
        'DESCRIPTION': "You'll use all your experience from the"
                       "break ins from before, and break into this factory."
                       "You will use your tool from before. You have made it"
                       "at the end of the hallway, there's a chest full of"
                       "limited flavored soups. You're finished. "
    }
}

current_node = world_map["ORPHANAGE"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP"]
playing = True

while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.upper()in directions:
        try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Recognized")
