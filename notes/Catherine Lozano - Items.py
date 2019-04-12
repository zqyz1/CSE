class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Key(Item):
    def __init__(self, name, description, unlocks):
        super(Key, self).__init__(name, description)
        self.unlocks = unlocks


class Chicken_Noodle_Soup(Item):
    def __init__(self, name, flavor, description):
        super(self, Chicken_Noodle_Soup).__init__(name, flavor)
        super().__init__(name, description)
        self.flavor = flavor


factory_key = Key("the Key to the Factory", "it unlocks the factory", factory)
meat_warehouse = Key("the key to the warehouse", "it unlocks the warehouse", warehouse)
onion_flavor = Chicken_Noodle_Soup("flavor chicken noodle soup", flavor)
rice_flavor = Chicken_Noodle_Soup("flavor chicken noodle soup", flavor)
fat_free = Chicken_Noodle_Soup("flavor chicken noodle soup", flavor)