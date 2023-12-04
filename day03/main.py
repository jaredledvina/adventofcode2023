#!/usr/bin/env python3
"""
Advent of Code - Day 3
"""
import os
from collections import defaultdict

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    return puzzle_input

def default_puzzle_map(puzzle_input):
    puzzle_dict = defaultdict(lambda: defaultdict(lambda: '.'))
    for y, line in enumerate(puzzle_input):
        for x, character in enumerate(line):
            puzzle_dict[x][y] = character
    return puzzle_dict


def is_symbol(character):
    return character != '.' and not character.isdigit()


def part1(puzzle_input):
    """
    >>> part1(['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.','...$.*....','.664.598..'])
    4361
    """
    puzzle_dict = default_puzzle_map(puzzle_input)
    part_total = 0
    for y, line in enumerate(puzzle_input):
        search_around = []
        part = ''
        end_of_line = len(line)-1
        for x, character in enumerate(line):
            if character.isdigit():
                search_around.append([x,y])
                part += character
            if not character.isdigit() or x == end_of_line:
                part_found = False
                for coordinate in search_around:
                    up = [coordinate[0], coordinate[1]-1]
                    down = [coordinate[0], coordinate[1]+1]
                    left = [coordinate[0]-1, coordinate[1]]
                    right = [coordinate[0]+1, coordinate[1]]
                    upleft = [coordinate[0]-1, coordinate[1]-1]
                    downleft = [coordinate[0]-1, coordinate[1]+1]
                    upright = [coordinate[0]+1, coordinate[1]-1]
                    downright = [coordinate[0]+1, coordinate[1]+1]
                    if is_symbol(puzzle_dict[up[0]][up[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[down[0]][down[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[left[0]][left[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[right[0]][right[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[upleft[0]][upleft[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[downleft[0]][downleft[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[upright[0]][upright[1]]):
                        part_found = True
                    elif is_symbol(puzzle_dict[downright[0]][downright[1]]):
                        part_found = True
                if part_found:
                    part_total += int(part)
                search_around = []
                part = ''
    return part_total


def find_gear(puzzle_dict, start_position):
    current_x = start_position[0]
    current_y = start_position[1]
    print('Start gear search at:', current_x, current_y, puzzle_dict[current_x][current_y])
    gear_start = False
    while not gear_start:
        if puzzle_dict[current_x-1][current_y].isdigit():
            current_x = current_x-1
        else:
            gear_start = True
    gear_end = False
    gear = ''
    while not gear_end:
        if puzzle_dict[current_x][current_y].isdigit():
            gear += puzzle_dict[current_x][current_y]
            current_x = current_x+1
        else:
            gear_end = True
        print("WIP gear:", gear)
    print("Final gear:", gear)
    return int(gear)


def part2(puzzle_input):
    """
    >>> part2(['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.','...$.*....','.664.598..'])
    467835
    """
    puzzle_dict = default_puzzle_map(puzzle_input)
    gear_ratio = 0
    for y, line in enumerate(puzzle_input):
        gears = set()
        for x, character in enumerate(line):
            if character == '*':
                print("Found * at:", x, y)
                coordinate = [x,y]
                current_gear_ratio = 0
                up = [coordinate[0], coordinate[1]-1]
                down = [coordinate[0], coordinate[1]+1]
                left = [coordinate[0]-1, coordinate[1]]
                right = [coordinate[0]+1, coordinate[1]]
                upleft = [coordinate[0]-1, coordinate[1]-1]
                downleft = [coordinate[0]-1, coordinate[1]+1]
                upright = [coordinate[0]+1, coordinate[1]-1]
                downright = [coordinate[0]+1, coordinate[1]+1]
                if puzzle_dict[up[0]][up[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, up))
                if puzzle_dict[down[0]][down[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, down))
                if puzzle_dict[left[0]][left[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, left))
                if puzzle_dict[right[0]][right[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, right))
                if puzzle_dict[upleft[0]][upleft[1]].isdigit():
                    print("upleft", puzzle_dict[upleft[0]][upleft[1]])
                    gears.add(find_gear(puzzle_dict, upleft))
                if puzzle_dict[downleft[0]][downleft[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, downleft))
                if puzzle_dict[upright[0]][upright[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, upright))
                if puzzle_dict[downright[0]][downright[1]].isdigit():
                    gears.add(find_gear(puzzle_dict, downright))
                print("Fucking gears", gears, len(gears))
                if len(gears) == 2:
                    print('Found gears:', gears)
                    gear_one = gears.pop()
                    gear_two = gears.pop()
                    current_gear_ratio = gear_one * gear_two
                    print('ratio', current_gear_ratio, 'gear_one', gear_one, 'gear_two', gear_two)
                    gears = set()
                gear_ratio += current_gear_ratio
                print('total_gear_ratio:', gear_ratio)
    return gear_ratio


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
