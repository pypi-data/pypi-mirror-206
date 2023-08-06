import random

class LiczbyLosowania():
    def __init__(self):
        self.min : int
        self.max : int
    def losujliczbe(self):
        liczba = random.randint(int(self.min), int(self.max))
        return liczba
