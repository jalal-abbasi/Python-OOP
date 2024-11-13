import random





class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = 'O'

    def __init__(self, is_computer=False):
        self._is_computer = is_computer

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
            computer_move = Move(computer_choice)
            return computer_move
        else:
            player_choice = int(input("please select a value between 1-9:"))
            player_move = Move(player_choice)
            return player_move


player = Player()
print(player.select_move())

