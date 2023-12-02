#!/usr/bin/env python3
"""
Advent of Code - Day 1
"""
import os

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    return puzzle_input


def part1(puzzle_input):
    """
    >>> part1(['1abc2','pqr3stu8vwx','a1b2c3d4e5','treb7uchet'])
    142
    """
    calibration = 0
    for line in puzzle_input:
        numbers = ''
        for character in line:
            if character.isdigit():
                numbers += character
        final_numbers = numbers[0] + numbers[-1]
        calibration = calibration + int(final_numbers)
    return calibration


def part2(puzzle_input):
    """
    >>> part2(['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen'])
    281
    """
    spelled_numbers = {
        'oneight': '18',
        'twone': '21',
        'threeight': '38',
        'fiveight': '58',
        'sevenine': '79',
        'eightwo': '82',
        'eighthree': '83',
        'nineight': '98',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    numbered_input = []
    for line in puzzle_input:
        for number in spelled_numbers.keys():
            line = line.replace(number, spelled_numbers[number])
        numbered_input.append(line)
    return part1(numbered_input)

def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
