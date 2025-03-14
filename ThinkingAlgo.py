from Game import Game
from random import randrange


class HunterBattleship():

    def __init__(self, game: 'Game'):

        self.game = game
        self.history = set()
        self.targets = []
        self.shots = 0


    def run(self) -> int:
        for i in range(1000):
            if len(self.targets) == 0:
                self.search_mode()
            else:
                self.hunter_mode()

        
            if self.game.game_done():
                break
        
        return self.shots

    def search_mode(self):
        x = randrange(0,10)
        y = randrange(0,10)

        if (x,y) in self.history:
            return
        
        if self.game.shoot(x, y):
            self.add_targets(x, y)

        self.history.add((x,y))

        self.shots += 1

    def hunter_mode(self):

        coords = self.targets.pop()

        if self.game.shoot(coords[0], coords[1]):
            self.add_targets(coords[0], coords[1])

        self.history.add((coords[0], coords[1]))

        self.shots += 1



    def add_targets(self, x: int, y: int) -> None:

        if x != 0 and (x - 1, y) not in self.history: 
            self.targets.append((x - 1, y))
        if x != 9 and (x + 1, y) not in self.history: 
            self.targets.append((x + 1, y))

        if y != 0 and (x, y - 1) not in self.history: 
            self.targets.append((x, y - 1))
        if y != 9 and (x, y + 1) not in self.history: 
            self.targets.append((x, y + 1))

    def reset(self) -> None:
        self.history = set()
        self.targets = []
        self.shots = 0
        self.game = Game()


if __name__ == '__main__':

    game = Game()
    simul = HunterBattleship(game)

    print(simul.run())
