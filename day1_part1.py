#!/usr/bin/env python

import sys

class CalibrationLine:
    def __init__(self, string):
        self.string = string
        self.reversed_string = string[-1::-1]
        self.first_number = self._get_first_number(self.string)
        self.last_number = self._get_first_number(self.reversed_string)
        self.value = 10 * self.first_number + self.last_number

    def _get_first_number(self, string):
        for character in string:
            if character.isdigit():
                return int(character)

def main():
    with open(sys.argv[1], 'r') as file_handle:
        sum_calibration_values = 0
        for line in file_handle:
            calibration_line = CalibrationLine(line)
            sum_calibration_values += calibration_line.value
    print(sum_calibration_values)

if __name__ == "__main__":
    main()