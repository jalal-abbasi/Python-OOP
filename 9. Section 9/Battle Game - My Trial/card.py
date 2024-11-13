from suits import Suits

class Card:
    #these are wrong! I should add the symbols in the suit class
    
    Values = {2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14}

    #here for Special_c I could have written a dictionary
    #Special_c = {"Jack" , "Queen", "King", "Ace"}
    Special_c = {11:"Jack" , 12: "Queen", 13: "King", 14: "Ace"}

   
    
    
    #these are correct
    def __init__(self, value, suit):
        self._value = value
        self._suit= suit 

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit

    #here the instructor has two methodes: show cards and is_special
    #the below is WRRong! when you make a class, it means that you are making sth that is represntative of sth general. so card is sth general 
    #that we can use it to make cards!!
        '''
    index = 0

    def make_card(self):
        self.cards = {}
        for item in Card.Suits:
            for num in Card.Values:
                if num > 10:
                    num = Card.Special_c[Card.index]
                    Card.index += 1
                self.cards[item] = num
        return self.cards
        '''

    #We usually use the attributes inside the methode
    #Inside the methode, we put "Parameters", not the object itself, since the object is represeted by self
    def is_special(self):

        #is it true? can we write it also for a dictionary?
        return self.value in Card.Special_c

    #we intorduce methodes inisde the class so that we can do the same functionality for all of the objects of the same class
    # (???)
    def show_card(self):
        if Card.is_special(self):
            self.value = Card.Special_c[self.value]
        return self.value , self.suit

    
    

    

