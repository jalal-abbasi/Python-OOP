"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class WarCardGame:

    # we add this values and assign them to theses because we want to add our code readability and write it in a more concise way
    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    #what do we need to have a game? we need a deck and two players.
    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck
    # we add this so that we generate the deck automatically whenever we call the Class
        self.make_initial_decks()

    #we introduce this methode to generate our deck. here again we do not have to import the other classes.
    # first we shuffle the cards
    # then we assign the shuffled cards to each of the players automatially after we shuffle the cards

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    # in this method we make the deck for each of the players, from the deck we draw a cards and then we add it 
    # to the character (i.e the player) as a sign of assigning the cards to that player. the thing is that we would
    # have say that we should take the cards from the shuffled deck. It is True, but in oop, we just write the methodes
    # independently from each other. we just write what functionality we expect from them other than what is going inside
    # the methode. we just want to operate what will come inside it. exactly like a function does!
    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    
    # now we have two states of the game. one is called battled which is when one of the cards is higher than the other
    # while the other state is called war, in which we have the same values of the cards, and so each player should
    # draw 3 other cards faced down, and the forth one will be evaluated as before (the higher value wins)

    # here, for battle we by default assume that we have a pure battle and no cards have been accumulate becuase of tie.
    def start_battle(self, cards_from_war=None):

        print("\n== Let's Start the Battle ==\n")

        # here we draw one card for each of the characters
        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        # here we are showing the cards for each of the players
        print(f"Your Card:")
        player_card.show()

        print(f"\nComputer Card: ")
        computer_card.show()

        # here, using the methodes get_round_winner and get_cards_wons (which both have not been defined yet)
        # we are first, determinning who is the winner then we are gathering the cards won.
        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        # here we are printing some messages whether the player has won or not and then adding (allocating) the cards
        # won to the winner
        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")

        # add cards to the character methode is a methode to add the cards to the character. we have two arguments
        # first we specify the winner, then we give the cards won to him/her or to the computer.
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")

            # here we have to implement the methode designed for the tie case. we have not defined it yet.
            self.start_war(cards_won)

        return winner


    # this is the definition of the methode used in line 63. it just gets the two cards and then compare them
    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE # this highlights the importance of defining the state of the game withh numbers
            # remember that in the class constants we said that the we impose Tie = 2.

    # here for get_cards_won we just gathered all the cards won by each round, taking also into account the 
    # possibility of having a tie
    def get_cards_won(self, player_card, computer_card, previous_cards):
        # this is very nice. remember that whenever we have an empty list, if we use conditionals for it, it will
        # apper as a False, otherwise it will return as a True (like here)
        # this is also nice. first we just put the two cards inside a list. then with a normal + we just summed the
        # two lists
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    # This is also used when we are going to add the cards to a character. just we add it to the LIST "character"
    # one by one, using a for loop and also by using the methode add_card we had in player Class.
    def add_cards_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    # here is the definition of when we have a tie. when we have a tie, we need some arguments. first we need
    # three cards from each character. we need the leading card played and also we need to play another card. 

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        # in the Player class, we have defined the players and also we defined a deck to them. so here
        # we are drawing the card three times from the top of each characters deck, and then append them 
        # to an empty list so that we can use it later as we are going to give all the gathered cards to the
        # winner
        for i in range(3):
            player_card = self._player.draw_card()
            player_cards.append(player_card)

            computer_card = self._computer.draw_card()
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")

        #here, we are calling the battle methode, since now the winner is determined through the forth card played, 
        # not that this methode doesn't accept any argument execpt we have cards accumulated from war (which is the case here)
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    # here we are determining when the game is over. the game is over when either of the players has nothing in deck.
    # has_empty_deck is from the Player class.
    def check_game_over(self):
        if self._player.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print("Try again. The computer won.")
            return True
        elif self._computer.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"Excellent. You won, {self._player.name}! Congratulations.")
            return True
        else:
            # for consistency of the code
            return False

    def print_stats(self):
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"The computer has {self._computer.deck.size} cards on its deck.")
        print("----")

    def print_welcome_message(self):
        print("==============================")
        print("|        War Card Game       |")
        print("==============================")

# for writting in POOP, consider pay attention to the type of each object to have a better intuition when 
# writting the code. for example, in line 159, we noq that player, is from Player class, which has a deck. 
# we know also that the deck is from Deck class, which has an attribute called size. so here we go!