__author__ = "Evgeny Kazanov"

import random


class Roulette:

    def check_colour(self, square_num, bet_colour):
        if square_num == 0:
            return False
        if (square_num % 2) == 0:
            colour = "black"
        else:
            colour = "red"
        return colour == bet_colour

    def spin(self, bet_colour):
        square_num = random.randint(0, 36)
        result = self.check_colour(square_num, bet_colour)
        return result

if __name__ == "__main__":
    roulette = Roulette()
    bet_colour = "red"
    print(f"bet_colour = {bet_colour}")
    result = roulette.spin(bet_colour)
    print(f"result = {result}")
