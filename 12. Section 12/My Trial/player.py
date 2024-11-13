import random

from move import Move


class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = 'O'

    def __init__(self, is_computer=False):
        self._is_computer = is_computer
        self._move = None

        if self._is_computer:
            self._marker = Player.COMPUTER_MARKER
        else:
            self._marker = Player.PLAYER_MARKER

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def marker(self):
        return self._marker

    def select_move(self):
        if self._is_computer:
            computer_choice = int(random.choice(range(1, 10)))
            self._move = Move(computer_choice)
            return self._move
        else:
            while True:
                player_choice = input("please select a value between 1-9: ")
                if player_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self._move = Move(int(player_choice))
                    break
                else:
                    print("please enter an integer value between 1 and 9: ")
            return self._move

    def is_player_choice_valid(self):
        return self._move.is_valid()







