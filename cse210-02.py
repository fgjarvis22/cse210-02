
import random

class Turn: 

    def __init__(self, name, score):
        self.score = score
        self.name = name
        self.players = []

    def get_score(self):
        return self.score 

class Game:

    players = []

    def num_players():
        x = 1
        player_count = int(input("How many players? "))
        while player_count > 0:
            player_name = input(f"What is player {x}'s name: ")
            new_player = Turn(player_name,300)
            Game.players.append(new_player)
            x +=1 
            player_count -= 1

        
    def main():
        Game.num_players()
        print(Game.players[0].score)
        return
        

Game.main()