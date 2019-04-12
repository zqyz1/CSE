class Computer(object):
    def __init__(self, brand, storage_type, capacity):
        self.brand = brand
        self.storage_type = storage_type
        self.mouse = True
        self.capacity = capacity
        self.keyboard = False

    def typing(self):
        if self.keyboard:
            print("Ypu aren't typing on the computer")

    def click(self):
        if self.mouse:
            print("You're clicking with the mouse")


my_computer = Computer("It's an apple computer", "It has an external hard drive", "The capacity is 500 gigabytes")
my_computer.typing()
