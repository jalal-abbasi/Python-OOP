"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Card:

    # we have to introduce the class constants to specifiy the special cards
    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
    # cards have only two attributes, the value and the suit
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    #we want to make our object do sth, or do sth with out object, so thats why we add the methode
    #here we want to show the value of the cards
    def show(self):
        card_value = self._value
        #here is very impotant. although we havn't imported the suit class, we write the suit as it has description and
        #symbol as attributes. so the attribute we are going to introduce in the future, will be a suit object as well
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")

    #this only returns true or false
    def is_special(self):
        return self._value >= 11
