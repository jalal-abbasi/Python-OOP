from card import Card
import random

class Deck:
    def __init__(self):
        self.deck = []


    def make_deck(self):
        index = 0
        for item in Card.Suits:
            for count in Card.Values:
                self.deck[index] = [Card.Suits, Card.Values]
                index +=1


    #the parameter inside the methode is just a parameter, so doesn't need to introduced beforehand
    #methode adds functionality to our class, for example for the deck, we want the deck to be shuffled and also divided.
    #or in the example of backpack we want our bacjpax=ck to add/ remove or to check the items in it.
    def shuffle_cards(self):
        #we must firt run make_deck to then shuffle the cards, so we must call the firt methode inside the second
        Deck.make_deck(self)
        cards_shuffled = random.shuffle(self.deck)
        return  cards_shuffled

    def divide_deck(self, index=False):
        cards = Deck.shuffle_cards(self)
        part_1 =[]
        k = 0

        for item in range(0,26):
            part_1[item] = cards.pop(item)

        if index or k==1:
            return cards
        elif not index:
            k+=1
            return part_1
        else:
            return 0




        
            




    
