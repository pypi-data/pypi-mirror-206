import random

class LiczbyLosowania():
    def __init__(self):
        return
    def losujliczbe(self, min : int = 0, max : int = 100):
        liczba = random.randint(int(min), int(max))
        return liczba
