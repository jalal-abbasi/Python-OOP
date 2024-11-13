"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
    #I had forgotten to introduce the suit class:
class Suit:
    #I shoulf have had added the symbols here as a dictionaty:
    SYMBOLS = {"clubs": "♣", "diamonds": "♦", "hearts": "♥", "spades": "♠"}
    #for being able to construct the suit (to know the attributes), we need the name of the suit and the symbol
    # but, since the by knowing the name we can have the symbol from the symbols constant abovs, we only need to 
    # introduce one argument but we still have two attributes!

    #WHAT ARE THE TWO MAIN ATTRIBUTES OF A SUIT? 1-NAME 2-SYMBOL
    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]
        #to make sure that the name that user enters is in lower case
        #we have to write the name if the class at the beginning even if we are going to use the class constant in the same class

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol
