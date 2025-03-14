from Game import Game;
from random_algo import RandomBattleship, ImprovedRandomBattleship
from ThinkingAlgo import HunterBattleship, ParityBattleship, FullKnowledgeBattleship
import pandas as pd



def runSimulations(controller, games=1_000_000):
    total_shots = 0
    data = pd.Series([0]*games)

    for i in range(games):
        shots = controller.run()
        total_shots += shots
        data.loc[i] = shots
        controller.reset()

    avg = total_shots/games



    print(f"Average shots in {games} games: {avg}")
    print("Stats:")
    print(data.describe())


print("Running completely random Algorithm")
game = Game()
controller = RandomBattleship(game)
runSimulations(controller)


print("Running improved random Algorithm")
game = Game()
controller = ImprovedRandomBattleship(game)
runSimulations(controller)

print("Running hunter Algorithm")
game = Game()
controller = HunterBattleship(game)
runSimulations(controller)

print("Running Parity Algorithm")
game = Game()
controller = ParityBattleship(game)
runSimulations(controller)

print("Running Full knowledge Algorithm")
game = Game()
controller = FullKnowledgeBattleship(game)
runSimulations(controller)


