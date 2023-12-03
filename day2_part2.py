#!/usr/bin/env python

import sys
import re

class ElfGame:
    def __init__(self, game_string):
        self.game_outcomes = re.sub('^.*:\s+', "", game_string.rstrip())
        self.cube_power = self._calculate_cube_power()

    def _calculate_cube_power(self):
        cube_power_value = 1
        color_cubes = {}
        reveals = self.game_outcomes.split(';')
        for reveal in reveals:
            draws = reveal.split(',')
            for draw in draws:
                balls, color = draw.split()
                if color in color_cubes and color_cubes[color] >= int(balls):
                    continue
                else:
                    color_cubes[color] = int(balls)
        for value in color_cubes.values():
            cube_power_value *= value
        return cube_power_value

def main():
    sum_cube_powers = 0
    with open(sys.argv[1], 'r') as fh:
        for line in fh:
            elf_game = ElfGame(line)
            sum_cube_powers += elf_game.cube_power
    print(sum_cube_powers)

if __name__ == "__main__":
    main()