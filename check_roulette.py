__author__ = "Evgeny Kazanov"

import random

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

    def __init__(self, roulette, wallet, goal_amount, first_bet, verbose=False):
        self.roulette = roulette
        self.wallet = wallet
        self.goal_amount = goal_amount
        self.first_bet = first_bet
        self.bet_colour = Colour.RED
        # self.session_num = session_num
        self.verbose = verbose

    def play_once(self, bet_value):
        result = self.roulette.spin(self.bet_colour)
        if result:
            self.wallet += bet_value
        else:
            self.wallet -= bet_value
        return result

    def play_to_end(self):
        n = 0
        bet = self.first_bet
        while True:
            n += 1
            result = self.play_once(bet)
            print_verbose(f"n: {n}, wallet: {self.wallet}, bet: {bet}, win: {result}",
                          verbose=self.verbose)
            if self.wallet == 0:
                break
            if not result:
                bet = bet * 2
            if self.wallet < bet:
                print_verbose("It is not enough money to double the bet. Bet all the wallet money.",
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
        print_verbose(f"{result} wallet: {self.wallet}, spins: {spins}", verbose=self.verbose)

    # def play_multisession(self):


if __name__ == "__main__":

    bet_colour = Colour.RED
    wallet = 10
    first_bet = 1
    goal_amount = 45
    verbose = True

    roulette = Roulette()
    game = Game(roulette=roulette,
                wallet=wallet,
                first_bet=first_bet,
                goal_amount=goal_amount,
                verbose=verbose
                )
    game.play_to_end()
