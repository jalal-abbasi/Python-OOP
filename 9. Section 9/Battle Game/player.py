"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
#The classes located in the same package do not have to be imported
#the whole point of this class is to assign a deck to the player (this was one of my main doubts)
class Player:

    #here we get the players name and also the deck which is assigned to that player. also, we write the is_computer
    # so that to know that we have by default that the we have real players.
    def __init__(self, name, deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer

    # we introduce a getter for the computer
    @property
    def is_computer(self):
        return self._is_computer


    # we also introduce a getter for the deck
    @property
    def deck(self):
        return self._deck

    # here we define this methode to know wether we have an empty deck for the player or not.
    def has_empty_deck(self):
        #if the deck is empty the below line of code will return true
        return self._deck.size == 0

    # here also we introduce another methode to draw a card from the deck of the player. (despite we have introduced)
    # it before in the deck class, we here introduce it again, for obtaining cards from the playeres deck.
    def draw_card(self):
        #here we say that if the deck of the player is not empty ( not false = true), draw a card form the deck
        #using the methode we have introduced in the Deck class
        #pay attention: whether we use the methode inside its own class or we use another class from another class, 
        #we do not need to implement self, as an argument inside the methode itself.

        #question??: why didn't we imported th Deck class, even if we are using this class in the player file?! the same we did in 
        #the deck file
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        self._deck.add(card)
