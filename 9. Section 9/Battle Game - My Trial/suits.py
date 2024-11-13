
class Suits:
   
    Symbols = {"hearts":"♥", "spades": "♠", "diamonds": "♦", "clubs": "♣"}

    
    def __init__(self, name):
        self._name = name
        
        self._symbol = Suits.Symbols[name.lower()]

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

        