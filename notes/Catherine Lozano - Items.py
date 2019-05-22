class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Key(Item):
    def __init__(self, name, description, unlocks):
        super(Key, self).__init__(name, description)
        self.unlocks = unlocks


class Food(Item):
    def __init__(self, name, flavor, description):
        super(self, Food).__init__(name, flavor)
        super().__init__(name, description)
        self.flavor = flavor


class chicken_soup(Food):
    def __init__(self, flavor):
        super(chicken_soup, self).__init__("chicken soup", "onion flavor", "onion flavored soup is a fat free food")
        self.flavor = flavor


class chicken_soup_2(Food):
    def __init__(self):
        super(chicken_soup_2, self).__init__("chicken soup", "spicy flavor",
                                             "one of the flavors that chicken noodle soup has is spicy flavor")


class chicken_soup_3(Food):
    def __init__(self):
        super(chicken_soup_3, self).__init__("chicken soup", "beef flavor", "another flavor you can find is beef")


class chicken_soup_4(Food):
    def __init__(self):
        super(chicken_soup_4, self).__init__("chicken soup", "chicken flavor", "another flavor you can find is chicken")


class chicken_soup_5(Food):
    def __init__(self):
        super(chicken_soup_5, self).__init__("chicken soup", "shrimp flavor", "another flavor you can find is shrimp")


class chicken_soup_6(Food):
    def __init__(self):
        super(chicken_soup_6, self).__init__("chicken soup", "chipotle flavor", "another flavor you can find is "
                                                                                "chipotle")


class chicken_soup_7(Food):
    def __init__(self):
        super(chicken_soup_7, self).__init__("chicken soup", "sriracha flavor", "another flavor you can find is "
                                                                                "sriracha")


class chicken_soup_8(Food):
    def __init__(self):
        super(chicken_soup_8, self).__init__("chicken soup", "lime flavor", "another flavor you can find is lime")


class chicken_soup_9(Food):
    def __init__(self):
        super(chicken_soup_9, self).__init__("chicken soup", "cheddar flavor", "another flavor you can find is cheddar")


class chicken_soup_10(Food):
    def __init__(self):
        super(chicken_soup_10, self).__init__("chicken soup", "roast chicken flavor", "another flavor you can find is"
                                                                                      "roast chicken")


class chicken_soup_11(Food):
    def __init__(self):
        super(chicken_soup_11, self).__init__("chicken soup", "broccoli flavor", "another flavor you can find is "
                                                                                 "broccoli")


class chicken_soup_12(Food):
    def __init__(self):
        super(chicken_soup_12, self).__init__("chicken soup", "tomato flavor", "another flavor you can find is tomato")


class chicken_soup_13(Food):
    def __init__(self):
        super(chicken_soup_13, self).__init__("chicken soup", "rice flavor", "another flavor you can find is rice")


class chicken_soup_14(Food):
    def __init__(self):
        super(chicken_soup_14, self).__init__("chicken soup", "mushroom flavor", "another flavor you can find is "
                                                                                 "mushroom")


class chicken_soup_15(Food):
    def __init__(self):
        super(chicken_soup_15, self).__init__("chicken soup", "green pea flavor", "another flavor you can find is green"
                                                                                  "pea")
