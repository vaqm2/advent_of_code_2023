#!/usr/bin/env python

import sys

class CalibrationLine:
    def __init__(self, string):
        self.string = string
        self.str_map = {'one' : 1, 
                        'two': 2, 
                        'three': 3,
                        'four' : 4,
                        'five': 5,
                        'six': 6,
                        'seven': 7,
                        'eight': 8,
                        'nine': 9}
        self.first_number = self._get_first_number()
        self.last_number = self._get_last_number()
        self.value = 10 * self.first_number + self.last_number

    def _get_first_number(self):
        iterated_substring = ''
        for character in self.string:
            if character.isdigit():
                return int(character)
            else:
                iterated_substring += character
                for key in self.str_map.keys():
                    if key in iterated_substring:
                        return self.str_map[key]
                
    def _get_last_number(self):
        iterated_substring = ''
        for character in reversed(self.string):
            if character.isdigit():
                return int(character)
            else:
                iterated_substring = character + iterated_substring
                for key in self.str_map.keys():
                    if key in iterated_substring:
                        return self.str_map[key]
            
def main():
    sum_calibration_values = 0
    with open(sys.argv[1], 'r') as file_handle:
        for line in file_handle:
            calibration_line = CalibrationLine(line.rstrip())
            sum_calibration_values += calibration_line.value
    file_handle.close()
    print(sum_calibration_values)

if __name__ == "__main__":
    main()