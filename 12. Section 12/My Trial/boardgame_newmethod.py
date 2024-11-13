from move import Move
from player import Player


class BoardGame:
    DEFAULT_VALUE = 0

    def __init__(self):
        self._initial_board = [[0, 0, 0]
                              ,[0, 0, 0]
                              ,[0, 0, 0]]
        self._player = Player()
        self._computer = Player(True)

    @property
    def initial_board(self):
        return self._initial_board

    def welcome_to_game(self):
        print("===========================================")
        print("welcome to the game! \n")
        print("===========================================/n")

    def show_numbers_position(self):
        print("the position of the numbers are as follow:\n")
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")

    def get_player_choice(self, player):

        player_move = player.select_move()  # player's move object
        row = player_move.get_row()
        col = player_move.get_column()

        if player.is_computer:  # printing the value
            print("the computer move is :", player_move.value)

        else:
            print("the player move is :", player_move.value)

        if self._initial_board[row][col]:
            print("that position is already taken is already taken. take care next time\n")
        else:
            self._initial_board[row][col] = player.marker

        return self._initial_board[row][col]

    def show_updated_board(self, player):
        diag_count = 0
        anti_diag_count = 0
        for row in [0, 1, 2]:
            if self._initial_board[row][row] == player.marker:
                diag_count += 1
            elif self._initial_board[row][2 - row] == player.marker:
                anti_diag_count += 1

            if anti_diag_count == 3 or diag_count == 3:
                return 1

            vertical_count = 0
            horizontal_count = 0

            for col in [0, 1, 2]:

                if self._initial_board[row][col] != 0:
                    print(" |", self._initial_board[row][col], end="")
                    if self._initial_board[row][col] == player.marker:
                        horizontal_count += 1
                    elif self._initial_board[col][row] == player.marker:
                        vertical_count += 1

                else:
                    print(" |", " ", end="")

                if col == 2:
                    print(" |\n")
            if horizontal_count == 3 or vertical_count == 3:
                return 1


    def check_tie(self):
        tie_count = 0
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if self._initial_board[row][col] != 0:
                    tie_count += 1

        if tie_count == 9:
            return 1

    def declare_winner(self, player):
        if player.is_computer:
            print("the computer won the game!")
            print("\n ========================")
            print("game is over!")
            print("===========================")

        else:
            print("the player won the game!")
            print("\n ========================")
            print("the game is over!")
            print("===========================")
        return 1

    def declare_tie(self):
        print("it's a tie!")
        print("\n ========================")
        print("the game is over!")
        print("===========================")
        return 1

    def check_game_over(self, player):
        if self.show_updated_board(player):
            return self.declare_winner(player)
        elif self.check_tie():
            return self.declare_tie()

    def start_game(self):
        self.welcome_to_game()
        counter = 1
        while True:
            print("=================================")
            print(f" this is the round # {counter} \n")
            counter += 1
            self.show_numbers_position()
            self.get_player_choice(self._player)
            if self.check_game_over(self._player) :
                break

            print("\n")
            self.get_player_choice(self._computer)
            if self.check_game_over(self._computer):
                break

game = BoardGame()
game.start_game()






