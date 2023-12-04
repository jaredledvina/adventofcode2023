#!/usr/bin/env python3
"""
Advent of Code - Day 4
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
    >>> part1(['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53','Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19','Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1','Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83','Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36','Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'])
    13
    """
    total_points = 0
    for card_line in puzzle_input:
        card_winners = 0
        card_points = 0
        _, cards = card_line.split(':')
        winning, scratched = cards.split('|')
        for number in winning.strip().replace('  ', ' ').split(' '):
            for scratch in scratched.strip().replace('  ', ' ').split(' '):
                if number == scratch:
                    card_winners += 1
        if card_winners:
            card_points = 2 ** (card_winners - 1)
        total_points += card_points
    return total_points



def part2(puzzle_input):
    """
    >>> part2(['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53','Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19','Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1','Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83','Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36','Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'])
    30
    """
    card_counts = {}
    for index, _ in enumerate(puzzle_input):
        card_counts[index] = 1
    for index, card_line in enumerate(puzzle_input):
        for copy in range(card_counts[index]):
            card_winners = 0
            _, cards = card_line.split(':')
            winning, scratched = cards.split('|')
            for number in winning.strip().replace('  ', ' ').split(' '):
                for scratch in scratched.strip().replace('  ', ' ').split(' '):
                    if number == scratch:
                        card_winners += 1
            for copy in range(1, card_winners+1):
                card_counts[index+copy] += 1
    return sum(card_counts.values())


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
