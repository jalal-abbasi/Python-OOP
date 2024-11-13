"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

import random
from card import Card
from suit import Suit


class Deck:

    #we can introduce the variable that we need for introducing a new methode as a class constant.
    SUITS = ("clubs", "diamonds", "hearts", "spades")


    #self is like the general name for the object, so it is like instead of writting my_list.append(), that my_list is
    #a specific motherfucking list, we can write self.append(), so that we are using the methode append() for the list class (all list objects in general)
    # here we write is empty, so to highlight wether out deck is initially empty or not. by defualt it is not.
    def __init__(self, is_empty=False):
        self._cards = []
    # here we bring the build methode here so that the deck be build whenever we call the Deck class. note how do we call the methode inside the class itself
    # self.methode(), here we do not have any argument inside. so when we are calling a methode we do not put the self argument inside it.
    #self.methode() is because the methode that we are using is from the class itself, so we write the self in the beginning, instead of a specific object.
        if not is_empty:
            self.build()

    #this property is the other way of accessing the attribute indirectly. here first of all, we have not defined the 
    #the size attribute inside the init methode, since it is dependent to the other attribute self._cards. secondly, we return 
    #the length (different from the getter case in which we had returned the attribute itself)
    @property
    def size(self):
        return len(self._cards)

    #here we have to import the two previous classes because we are calling the methodes. but previously we
    #were saying that the attribute that currently I am talking about will be introduced as an object in the future.
    def build(self):

        #so the Class Constant we have introduced is used here.
        for suit in Deck.SUITS:
            for value in range(2, 15):
                
                #here since we are calling a methode from another classes we are importing those calsses.
                #here, IS VERY VERY IMPORTANT:
                #here this is the answer to the question I also had!
                #here basically we are introducing a specific object for every loop and then putting it inside the 
                # the cards. just instead of assiging it to a variable we write it directly. so it should have been like
                # my_card = Card(Suit(suit), value))
                #the other point is the Suit attribute. as we said, we knew already that the suit as an attribute of 
                #the Card, will be Suit object. so we have written. my_suit = Suit(suit) (the suit is a description of the card,  so clubs, hearts, etc)
        
                self._cards.append(Card(Suit(suit), value))

    #This is the a methode to show all cards. note that the card.show() is a methode coming from the class methode.
    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        #shuffle methode is coming from the random class
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        # to be consistent with the coding we also return none when using else in this case.
        else:
            return None

    #to add a card to the bottom of the card stack
    #here look that this methode has an argument card. that we know that it will be an object in the future when
    # we run the main code
    def add(self, card):
        self._cards.insert(0, card)


    # so basically the methode is all the action that we can do with the object that we have. for exampe for a 
    #backpack we can add sth, we can remove, we can check sth or so on. here also for the dexk , we can shuffle it, 
    # we can remove cards, or add cards, and we can show cards.
