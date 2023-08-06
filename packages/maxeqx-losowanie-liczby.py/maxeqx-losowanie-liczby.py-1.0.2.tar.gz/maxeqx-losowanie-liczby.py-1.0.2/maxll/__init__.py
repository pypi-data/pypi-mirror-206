import random

class LiczbyLosowania():
    def __init__(self):
        return
    def losujliczbe(self, min : int, max : int):
        liczba = random.randint(int(min), int(max))
        return liczba
