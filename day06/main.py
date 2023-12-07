#!/usr/bin/env python3
"""
Advent of Code - Day 6
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
    >>> part1(['Time:      7  15   30','Distance:  9  40  200'])
    288
    """
    times = puzzle_input[0].split()[1:]
    distances = puzzle_input[1].split()[1:]
    overall_winners = 1
    for time, distance in zip(times, distances):
        distance = int(distance)
        time = int(time)
        winners = 0
        for held_time in range(1, time-1):
            if held_time * (time - held_time) > distance:
                winners += 1
        overall_winners = overall_winners * winners
    return overall_winners




def part2(puzzle_input):
    """
    >>> part2(['Time:      7  15   30','Distance:  9  40  200'])
    71503
    """
    time = int("".join(puzzle_input[0].split()[1:]))
    distance = int("".join(puzzle_input[1].split()[1:]))
    winners = 0
    for held_time in range(1, time-1):
        if held_time * (time - held_time) > distance:
                winners += 1
    return winners



def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
