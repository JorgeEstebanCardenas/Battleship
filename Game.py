import os
from Ship import Ship
from logger_setup import setup_logger
from Board import Board
from colorama import init, Fore, Style

class Game():

    def __init__(self):
        self.logger = setup_logger()
        self.board = Board()
        self.shots = 0

        init()

        self.setup_ships()

    def start_game(self):
        finished = False

        print("Game is starting")            
        print("===================================")


        while not finished:
            self.display()
            
            finished = self.handle_input()

            if self.board.remaining_hits <= 0:
                finished = True
                self.print_stats()


            
    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')


    def display(self) -> None:
        self.board.print()


    def handle_input(self) -> bool:
        user_input = input("Enter two integers separated by a space (or press Enter to quit): ")
        


        if not user_input.strip():
            self.print_stats()
            return True

        try:
            x, y = map(int, user_input.split())

            print("===================================")

   
            if self.shoot(x, y):
                print(Fore.RED + f"Hit on ({x},{y})" + Style.RESET_ALL)
            else:
                print(f"Miss on ({x},{y})")

            self.shots += 1


        except ValueError:
            print(Fore.YELLOW + "Invalid input. Please enter two integers." + Style.RESET_ALL)

            print("===================================")



        
        return False

    def print_stats(self) -> None:
        print("===================================")
        print("Game ended\n")

        if self.board.remaining_hits == 0:
            print(Fore.GREEN + "YOU WIN" + Style.RESET_ALL)

        print("\nGAME STATS")

        print("----------------------------------")

        print(f"Total shots: {self.shots}")
        print(f"You got {self.board.total_hits - self.board.remaining_hits} out of {self.board.total_hits} hits")
        print(f"Hit rate: {self.get_hit_rate():.0%} ({self.board.total_hits - self.board.remaining_hits} out of {self.shots})")


    def get_hit_rate(self) -> float:
        if self.shots == 0: return 0

        return ((self.board.total_hits - self.board.remaining_hits)/self.shots)


    def setup_ships(self) -> None:
        print("Setting up ships")

        self.board.add_ship(5)
        self.board.add_ship(4)
        self.board.add_ship(3)
        self.board.add_ship(3)
        self.board.add_ship(2)

    def shoot(self, x: int, y: int) -> bool:
        return self.board.check_for_ship(x,y)

   
        



if __name__ == '__main__':
    G = Game()

    G.start_game()
