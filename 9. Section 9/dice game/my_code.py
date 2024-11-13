import random


class Die:

    def __init__(self):
        self._value = self.roll_die()

    @property
    def value(self):
        return self._value

    def roll_die(self):
        return random.randint(1, 6)

    def show_dice(self):
        return self._value


class Player:

    def __init__(self, player_dice, counter=10, is_computer=False):
        self.dice = player_dice
        self.is_computer = is_computer
        self.counter = counter

    def roll_dice_player(self):
        return self.dice.roll_die()


class DiceGame:
    Round_Counter = 1

    def __init__(self, player_one, player_two):
        self._player_one = player_one
        self._player_two = player_two

    def start_game(self):
        print("==========================================")
        print("Welcome to the DiceGame")
        print("==========================================\n")

        while 1:
            print("\n")
            val = input("press any key")
            if not val:
                self.start_round()

            if self.game_over():
                break

    def start_round(self):
        print(f"round number {self.Round_Counter}")
        self.Round_Counter += 1

        p_1 = self._player_one.roll_dice_player()
        p_2 = self._player_two.roll_dice_player()

        print(f"player one dice value is {p_1}")
        print(f"player two dice value is {p_2} \n")
        if p_1 > p_2:
            print("player 1 wins")
            self._player_one.counter += 1
            self._player_two.counter -= 1
            print(f"player 1 counter is: {self._player_one.counter}")
            print(f"player 2 counter is : {self._player_two.counter}")
        elif p_2 > p_1:
            print("player 2 wins")
            self._player_one.counter -= 1
            self._player_two.counter += 1
            print(f"player 1 counter is: {self._player_one.counter}")
            print(f"player 2 counter is : {self._player_two.counter}")
        else:
            print("it is a draw!")
            print(f"player 1 counter is: {self._player_one.counter}")
            print(f"player 2 counter is : {self._player_two.counter}")









    def game_over(self):
        if self._player_one.counter == 0:
            print("\n player one wins the Game!")
            return 1

        elif self._player_two.counter == 0:
            print("\n player two wins the Game!")
            return 1





dice_1st = Die()
dice_2nd = Die()

player_1st = Player(dice_1st)
player_2nd = Player(dice_2nd, is_computer=True)

#print(player_1st.dice.value)
#print(player_2nd.dice.value)
my_game = DiceGame(player_1st, player_2nd)
my_game.start_game()









