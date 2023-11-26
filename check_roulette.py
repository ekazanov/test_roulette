__author__ = "Evgeny Kazanov"

import random
import argparse

def print_verbose(string, verbose=False):
    if verbose:
        print(string)

class Colour:
    RED = 1
    BLACK = 0

class Roulette:

    def check_colour(self, square_num, bet_colour):
        if square_num == 0:
            return False
        if (square_num % 2) == 0:
            colour = Colour.BLACK
        else:
            colour = Colour.RED
        return colour == bet_colour

    def spin(self, bet_colour):
        square_num = random.randint(0, 36)
        result = self.check_colour(square_num, bet_colour)
        return result

class Game:

    def __init__(self, roulette, wallet, goal_amount, first_bet,
                 verbose=False):
        self.roulette = roulette
        self.wallet = wallet
        self.goal_amount = goal_amount
        self.first_bet = first_bet
        self.bet_colour = Colour.RED
        self.verbose = verbose

    def play_once(self, bet_value):
        result = self.roulette.spin(self.bet_colour)
        if result:
            self.wallet += bet_value
        else:
            self.wallet -= bet_value
        return result

    def play_to_goal(self):
        n = 0
        bet = self.first_bet
        while True:
            n += 1
            wallet_before = self.wallet
            result = self.play_once(bet)
            print_verbose(f"n: {n}, wallet: {wallet_before}, bet: {bet}, \
won: {result}", verbose=self.verbose)
            if self.wallet == 0:
                break
            if not result:
                bet = bet * 2
            if self.wallet < bet:
                print_verbose("It is not enough money to double the bet. \
Bet the entire wallet.",
                              verbose=self.verbose)
                bet = self.wallet
            if self.wallet >= self.goal_amount:
                break
        self.print_session_report(n)

    def print_session_report(self, spins):
        if self.wallet > 0:
            result = "You won! "
        else:
            result = "You lost!"
        print_verbose("-"*40, verbose=self.verbose)
        print_verbose(f"{result} wallet: {self.wallet}, spins: {spins}",
                      verbose=self.verbose)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Roulette startegy testing program.')
    parser.add_argument('--wallet', "-w", type=int, required=True,
                        metavar='INTEGER', help="Wallet start amount")
    parser.add_argument('--first_bet', "-f", type=int,  required=True,
                        metavar='INTEGER', help="First bet value.")
    parser.add_argument('--goal_amount', "-g", type=int, required=True,
                        metavar='INTEGER', help="Give up when program \
has got this amount in the wallet.")
    parser.add_argument('--session_num', "-s", type=int,  required=True,
                        metavar='INTEGER', help="Number of game sessions to \
play. Int.")
    parser.add_argument('--verbose', "-v", type=int, default=0, choices=[0, 1],
                        metavar='INTEGER',  help="Verbosity level. 0/1")
    
    args = parser.parse_args()

    wallet = 10
    first_bet = 1
    goal_amount = 45
    session_num = 100
    verbose = False

    roulette = Roulette()
    session_result = 0
    for _ in range(args.session_num):
        game = Game(roulette=roulette,
                    wallet=args.wallet,
                    first_bet=args.first_bet,
                    goal_amount=args.goal_amount,
                    verbose=args.verbose,
                    )
        game.play_to_goal()
        if game.wallet > 0:
            session_result += 1
    print("-"*40)
    print("Result:")
    print(f"Session number: {args.session_num}, won: {session_result}, \
lost: {args.session_num - session_result}")
