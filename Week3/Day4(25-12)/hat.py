import random


class Hat:
    def __init__(self):
        self.houese = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name + " is in " + random.choice(self.houese))

hat = Hat()
hat.sort("Harry")

