from player import Player
class Game:
    def __init__(self) -> None:
        pass

    def drew_cards(self, cards):
        drew_c = cards.append(0)
        return drew_c
        
    def win_round(self, cards1, cards2):
        drew1 = Game.draw_cards(cards1)
        drew2 = Game.draw_cards(cards2)
        gathered =[]

        if drew1[1] > drew2[1]:
            print(f"{Player.name} won the round")
            cards1 += drew1 + drew2 + gathered
            

        elif drew1[1] < drew2[1]:
            print(f"computer won")
            cards2 += drew1 + drew2 + gathered

        else:
            gathered = drew1 + drew2
            for k in range(3):
                drew1 = Player.draw_cards(cards1)
                drew2 = Player.draw_cards(cards2)

                gathered += drew1 + drew2

                
