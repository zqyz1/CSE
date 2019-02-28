world_map = {
    'R19A': {
        'NAME': "Orphanage",
        'DESCRIPTION': "This is the room that you are in right "
                       "now. It has two exits, one's to the south of the room and the other to the east.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'HOSPITAL': {
        'NAME': "UCLA Medical Center",
        'DESCRIPTION': "There are cars parked here. To "
                       "the south is Mr. Wiebe's room",
        'PATHS': {
            'SOUTH': "R19A"
        }
    },
    'MEAT WAREHOUSE':{
        'NAME': "Butcher's Warehouse",
        'DESCRIPTION': "This is the most famous warehouse.",
        'PATHS': {
            'SOUTH': "R19A"
        }
    },
    'SCHOOL':{
        'NAME': "Edison High School",
        'DESCRIPTION': "This is the school you attend",
        'PATHS': {
            'EAST': "WOOD SHOP"
        }
    },
    'WOOD SHOP':{
        'NAME': "Sam's Wood Shop",
        'DESCRIPTION': "In this wood shop uou can grab a"
                       "hammer, to help you later on break "
                       "into the Chicken Noodle Soup Factory",
        'PATHS': {
            'SOUTH': "CEMETERY"
        }
    },
    'CEMETERY':{
        'NAME': "Animal Cemetery Center",
        'DESCRIPTION': "This cemetery is hard to go through"
                       "because of you parents burying your dog"
                       "here",
        'PATHS': {
            'EAST': "BOX"
        }
    },
    'BOX':{
        'NAME': "Catherine's Box",
        'DESCRIPTION': "This is where you live, you will go in the "
                       "box and garb a light, to help you along the way",
        'PATHS': {
            'SOUTH': "HOUSE"
        }
    },
    'HOUSE':{
        'NAME': "Delaney's House",
        'DESCRIPTION': "When you arrive to the house, you will have to "
                       "break in. It's an abandoned house, you will need "
                       "your flashlight to go through the house",
        'PATHS': {
            'WEST': "GROCERY STORE"
        }
    },
    'GROCERY STORE':{
        'NAME': "Sam's Grocery Store",
        'DESCRIPTION': "Here you will find food, you will eat whatever "
                       "helps you from starving to death",
        'PATHS': {
            'SOUTH': "SECRET DOOR"
        }
    },
    'SECRET DOOR':{
        'NAME': "Secret Door",
        'DESCRIPTION': "You have unlocked a secret room that leads you to"
                       "the apartments",
        'PATHS': {
            'WEST': "APARTMENT"
        }
    },
    'APARTMENT':{
        'NAME': "Sam's Apartment Village",
        'DESCRIPTION': "This is where you will be supplied with food,"
                       "you'll energy",
        'PATHS': {
            'SOUTH': "SHELTER"
        }
    },
    'SHELTER': {
        'NAME': "Homeless Shelter",
        'DESCRIPTION': ""
    }
}







current_node = world_map['R19A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
while playing:playing = True

    command = input 




