__author__ = "Evgeny Kazanov"

import random

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



if __name__ == "__main__":
    roulette = Roulette()
    bet_colour = Colour.RED
    wallet = 10
    start_bet = 1
    to_win = 45

    n = 0
    bet = start_bet
    while True:
        n += 1
        spin_result = roulette.spin(bet_colour)
        print(f"n: {n}, wallet: {wallet}, bet: {bet}, win: {spin_result};")
        if spin_result:
            wallet += bet
        else:
            wallet -= bet
            bet = bet * 2
        if wallet <=0:
            wallet = 0
            break
        if wallet < bet:
            print("It is not enough money to double the bet. Bet all the wallet money.")
            bet = wallet
        if wallet >= to_win:
            break

    # Print report
    print("-" * 40)
    if wallet > 0:
        print("You won!")
    else:
        print("You lost!")
    print(f"wallet = {wallet}")
    print(f"n = {n}")
