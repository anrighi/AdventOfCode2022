import os
import time
from utility.file_reader import FileReader


def part_1(value_list):

    points = 0

    for i in range(len(value_list)):

        starting_rucksack = value_list[i]

        rucksack_left = starting_rucksack[:int(len(starting_rucksack) / 2)]
        rucksack_right = starting_rucksack[int(len(starting_rucksack) / 2):]

        for item in rucksack_left:
            if item in rucksack_right:
                points += ord(item) - (96 if item.islower() else 38)
                break

    return points


def part_2(value_list):
    points = 0

    for i in range(len(value_list)):

        if i % 3 != 0 and i > 0:
            continue

        rucksack_first = value_list[i - 1]
        rucksack_second = value_list[i - 2]
        rucksack_third = value_list[i - 3]

        for item in rucksack_first:
            if item in rucksack_second and item in rucksack_third:
                points += ord(item) - (96 if item.islower() else 38)
                break

    return points


def main():

    start_time = time.time()
    print("--- day3 ---")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_reader = FileReader(dir_path + "/input.txt")
    input_read = file_reader.read_file("\n")

    print("--- parsing time: ---")
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 1: ", part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
