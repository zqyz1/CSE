class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class Player(object):
    def __init__(self, current_location):
        self.health = 100
        self.current_location = current_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """This method moves a character to a new location
        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


# Put them in quotes
orphanage = Room("Sam's Orphanage", "hospital", None, None, None,
                 "This is the room that you are in right "
                 "now. It has one exit. To the north is the hospital.")
hospital = Room("UCLA Medical Center", None, "meat_warehouse", None, None, "This is were sick patients come in, you'll"
                                                                           "have to pass by here to get to your "
                                                                           "destination. "
                                                                           "To the south is the meat warehouse.")
meat_warehouse = Room("Butcher's Warehouse", None, "school", None, None, "This is the most famous warehouse. To the "
                                                                         "south is the school.")

school = Room("Edison High School", None, None, "wood_shop", None, "This is the school you attend. "
                                                                   "To the east is the wood shop.")
wood_shop = Room("Sam's Wood Shop", None, "cemetery", None, None, "In this wood shop uou can grab a"
                                                                  "hammer, to help you later on break"
                                                                  "into the Chicken Noodle Soup Factory."
                                                                  "To the south is the cemetery.")
cemetery = Room("Animal Cemetery Center", None, None, "box", None, "This cemetery is hard to go through"
                                                                   "because of you parents burying your dog"
                                                                   "here. To the east is the box.")
box = Room("Catherine's Box", None, "house", None, None, "This is where you live, you will go in the "
                                                         "box and grab a light, to help you along the way."
                                                         "To the south is the house.")
house = Room("Delaney's House", None, None, None, "grocery_store", "Here you will find food, you will eat whatever "
                                                                   "helps you from starving to death. To the south"
                                                                   "is the secret door.")
grocery_store = Room("Sam's Grocery Store", None, "secret_door", None, None,
                     "Here you will find food, you will eat whatever "
                     "helps you from starving to death. To the south"
                     "is the secret door.")
secret_door = Room("Secret Door", None, None, None, "apartment", "You have unlocked a secret room that leads you to"
                                                                 "the apartments. You'll have to go west.")
apartment = Room("Sam'a Apartment Village", None, "shelter", None, None, "This is where you will be supplied with food,"
                                                                         "you'll need energy, it's to the south.")
shelter = Room("Homeless Shelter", None, "police_station", None, None, "In here you'll find wise homeless people,"
                                                                       "they'll give you some advise on how to break "
                                                                       "into the factory. "
                                                                       "Afterwards, head south, to the police station.")
police_station = Room("Police Station", None, "blueberry_farm", None, None,
                      "This is where you'll have a talk with the inmates,"
                      "you'll learn of many different ways to break into a"
                      "place. The information will help you. To the south is the blueberry farm.")
blueberry_farm = Room("Sam's Blueberry Farm", None, "blueberry_farm", None, None,
                      "In order to get to the Chicken Noodle SOup Factory, \n you'll need to break into this farm. "
                      "It's the only way. To the south is the blueberry factory.")
blueberry_factory = Room("Sam's Blueberry Factory", None, None, "soup_factory", None,
                         "You'll also have to break into the factory,"
                         "this break in will also prepare you for the "
                         "Chicken Noodle Soup Factory break in. To the east is the blueberry factory.")
soup_factory = Room("Chicken Noodle Soup Factory", None, None, None, None, "You'll use all your experience from the"
                                                                           "break ins from before, and break into "
                                                                           "this factory. "
                                                                           "You will use your tool from before. You "
                                                                           "have made it "
                                                                           "at the end of the hallway, there's a "
                                                                           "chest full of "
                                                                           "limited flavored soups. You're finished.")

# Players
player = Player(orphanage)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(player.current_location, command)
            
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("This key does not exist")
        except AttributeError:

            print("I can't go that way.")
    else:
        print("Command Not Recognized")