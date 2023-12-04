#!/usr/bin/env python3
"""
Advent of Code - Day 2
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
    >>> part1(['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red','Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'])
    8
    """
    color_maxes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible_game_id_sum = 0
    for line in puzzle_input:
        game_id, games = line.split(':')
        game_id = int(game_id.split(' ')[-1])
        games = games.split(';')
        impossible = False
        for game in games:
            colors = game.split(',')
            for color_draw in colors:
                _, number, color = color_draw.split(' ')
                if color_maxes[color] < int(number):
                    impossible = True
        if not impossible:
            possible_game_id_sum += game_id
    return possible_game_id_sum


def part2(puzzle_input):
    """
    >>> part2(['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red','Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'])
    2286
    """
    game_multiple_sum = 0
    for line in puzzle_input:
        game_mins = {
            'red': 1,
            'blue': 1,
            'green': 1
        }
        multiple = 1
        _, games = line.split(':')
        games = games.split(';')
        for game in games:
            colors = game.split(',')
            for color_draw in colors:
                _, number, color = color_draw.split(' ')
                if game_mins[color] < int(number):
                    game_mins[color] = int(number)
        for min in game_mins.values():
            multiple = min * multiple
        game_multiple_sum += multiple
    return game_multiple_sum


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
