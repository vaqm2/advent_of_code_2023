#!/usr/bin/env python

import sys

class ElfGame:
    def __init__(self, game_string, bag_contents):
        self.game_outcomes = game_string.lstrip('Game ').rstrip()
        self.bag_contents = bag_contents
        self.game_number, self.game_outcomes = self.game_outcomes.split(':')
        self.game_number = int(self.game_number)

    def is_possible(self):
        reveals = self.game_outcomes.split(';')
        for reveal in reveals:
            draws = reveal.split(',')
            for draw in draws:
                balls, color = draw.split()
                if self.bag_contents[color] < int(balls):
                    return False
        return True

def main():
    bag_contents = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_possible_games = 0
    with open(sys.argv[1], 'r') as fh:
        for line in fh:
            elf_game = ElfGame(line, bag_contents)
            if elf_game.is_possible():
                sum_of_possible_games += elf_game.game_number
    print(sum_of_possible_games)

if __name__ == "__main__":
    main()