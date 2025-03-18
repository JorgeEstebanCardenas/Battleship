from Battleship.Game import Game
from random import randrange


class RandomBattleship():

    def __init__(self, game: 'Game'):
        self.game = game
        self.shots = 0


    def run(self) -> int:
        while not self.game.game_done():

            x = randrange(0,10)
            y = randrange(0,10)

            self.game.shoot(x, y)

            self.shots += 1
        
        return self.shots
    
    def reset(self) -> None:
        self.shots = 0
        self.game = Game()
           

class ImprovedRandomBattleship():
    def __init__(self, game: 'Game'):
        self.game = game
        self.history = set()
        self.shots = 0


    def run(self) -> int:
        while not self.game.game_done():

            while True:
                x = randrange(0,10)
                y = randrange(0,10)

                if (x,y) not in self.history:
                    break

            self.game.shoot(x, y)

            self.shots += 1

            self.history.add((x,y))
        
        return self.shots
    
    def reset(self) -> None:
        self.shots = 0
        self.game = Game()
        self.history = set()

    
if __name__ == '__main__':

    game = Game()
    simul = RandomBattleship(game)

    print(f"Random {simul.run()}")

    game = Game()
    simul = ImprovedRandomBattleship(game)

    print(f"Improved {simul.run()}")

