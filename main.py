from Game import Game;
from random_algo import RandomBattleship, ImprovedRandomBattleship
from ThinkingAlgo import HunterBattleship


print("Running completely random Algorithm")

games = 100000
total_shots = 0

for _ in range(games):
    game = Game()
    randomB = RandomBattleship(game)

    total_shots += randomB.run()

avg = total_shots/games

print(f"Average shots in {games} games: {avg}")


print("Running improved random Algorithm")

games = 100000
total_shots = 0

for _ in range(games):
    game = Game()
    randomB = ImprovedRandomBattleship(game)

    total_shots += randomB.run()

avg = total_shots/games

print(f"Average shots in {games} games: {avg}")

print("Running Hunter Algorithm")

games = 100000
total_shots = 0

for _ in range(games):
    game = Game()
    randomB = HunterBattleship(game)

    total_shots += randomB.run()

avg = total_shots/games

print(f"Average shots in {games} games: {avg}")

