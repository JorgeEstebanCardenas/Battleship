from Game import Game;
from random_algo import RandomBattleship, ImprovedRandomBattleship
from ThinkingAlgo import HunterBattleship, ParityBattleship, FullKnowledgeBattleship
import pandas as pd



def runSimulations(controller, games=100_000):
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

    return data


print("Running completely random Algorithm")
game = Game()
controller = RandomBattleship(game)
random_data = runSimulations(controller)


print("Running improved random Algorithm")
game = Game()
controller = ImprovedRandomBattleship(game)
improved_data = runSimulations(controller)

print("Running hunter Algorithm")
game = Game()
controller = HunterBattleship(game)
hunter_data = runSimulations(controller)

print("Running Parity Algorithm")
game = Game()
controller = ParityBattleship(game)
parity_data = runSimulations(controller)

print("Running Full knowledge Algorithm")
game = Game()
controller = FullKnowledgeBattleship(game)
fullk_data = runSimulations(controller)


df = pd.DataFrame({
    "Random": random_data.sort_values().reset_index(drop=True),
    "Improved": improved_data.sort_values().reset_index(drop=True),
    "Hunter": hunter_data.sort_values().reset_index(drop=True),
    "Parity": parity_data.sort_values().reset_index(drop=True),
    "Full Knowledge": fullk_data.sort_values().reset_index(drop=True)
})

df.to_csv("./results.csv")