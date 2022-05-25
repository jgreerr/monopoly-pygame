from random import random
from board.board import Board
from board.space import *
from player import Player
from text import Text
import random

class CPU(Player):
    
    def __init__(self, color):
        super().__init__(color)

    def play(self, board : Board, texts : list[Text], players): 

        roll = random.randrange(2, 12)

        landed_on_space = self.move(roll, board)
        texts.append(Text(f"Player {self.id} rolled a {roll} and landed on {landed_on_space.space_name}", 0, 20)) 
        
        self.rectangle.x = landed_on_space.x
        self.rectangle.y = landed_on_space.y


        if landed_on_space.IS_BUYABLE:
            if (landed_on_space.owner == None):
                if self.money - landed_on_space.printed_price > 0:
                    self.buy(landed_on_space)
                else:
                    texts.append(Text("CPU can't afford to pay.", 0, 40))
            elif (landed_on_space.owner == self):
                texts.append(Text("CPU owns the property.", 0, 40))
            else:   
                if self.money - landed_on_space.get_current_price() > 0:
                    self.pay(landed_on_space.owner, landed_on_space)
                    texts.append(Text(f"CPU landed on Player {str(landed_on_space.owner.id)}'s "
                    f"property and paid them {landed_on_space.get_current_price()}$", 0, 40))
                else:
                    texts.append(Text(f"CPU landed on Player {str(landed_on_space.owner.id)}'s "
                    f"property and couldn't afford", 0, 40))
                    self.mortgage_des()

        elif type(landed_on_space) is Monopoly_Chance: 
            texts.append(landed_on_space.draw_card(self, players, board))  
        elif type(landed_on_space) is Monopoly_Community_Chest:
            texts.append(landed_on_space.draw_card(self, players, board))
        else:
            texts.append(Text("Not buyable.", 0, 40))

    def mortgage_des(self):
        print("test")