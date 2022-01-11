
import random

class Game:

    n = 0
    choice = 0
    score = 300 
    lose = 0

    def turn():
        Game.choice = input("Higher or lower? [h/l]: ")
        if Game.choice.lower() == 'l':
            x = random.randint(1,13)
            print(f"Next card was: {x}")
            if Game.n > x:
                Game.score = Game.score + 100 
            else:
                Game.score = Game.score - 75
        elif Game.choice.lower() == 'h':
            x = random.randint(1,13) 
            print(f"Next card was: {x}")
            if Game.n < x:
                Game.score = Game.score + 100 
            else:
                Game.score = Game.score - 75

    def check_loss():
        if Game.score == 0:
            Game.lose == 1
            print("Your score has reached 0\nYou lose...")

                
    def main():
        while True:
            Game.n = random.randint(1,13) 
            print(f"The card is: {Game.n}")
            Game.turn()
            print(f"Your score is: {Game.score}")
            Game.check_loss()
            if Game.lose == 1:
                break
            else:
                while True:
                    again = input("\nPlay again? [y/n]: ")
                    if again.lower() == 'y':
                        print()
                        Game.main()
                    elif again.lower() == 'n':
                        break
                    else:
                        print("Error! Please choose either 'y' or 'n'")
                break

Game.main()