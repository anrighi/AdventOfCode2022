import os
import time
from utility.file_reader import FileReader

points_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

meanings_dict = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

beats_dict = {
    "paper": "rock",
    "rock": "scissors",
    "scissors": "paper"
}

ends_dict = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}


def part_1(value_list):

    points = 0

    for i in range(len(value_list)):

        points += points_dict[value_list[i][1]]

        op_meaning = meanings_dict[value_list[i][0]]
        my_meaning = meanings_dict[value_list[i][1]]

        if op_meaning == my_meaning:
            points += 3
        elif beats_dict[my_meaning] == op_meaning:
            points += 6

    return points


def part_2(value_list):
    points = 0

    beats_keys = list(beats_dict.keys())
    beats_values = list(beats_dict.values())

    meanings_keys = list(meanings_dict.keys())
    meanings_values = list(meanings_dict.values())

    for i in range(len(value_list)):

        end = ends_dict[value_list[i][1]]
        op_meaning = meanings_dict[value_list[i][0]]

        if end == "win":
            points += 6
            my_choice = beats_keys[beats_values.index(op_meaning)]
        elif end == "draw":
            points += 3
            my_choice = meanings_dict[value_list[i][0]]
        else:
            my_choice = beats_dict[op_meaning]

        my_letter = meanings_keys[meanings_values.index(my_choice)]
        points += points_dict[my_letter]

    return points


def main():

    start_time = time.time()
    print("--- day2 ---")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_reader = FileReader(dir_path + "/input.txt")
    input_read = file_reader.read_file("\n")

    value_list = []

    for i in range(len(input_read)):
        value_list.append(input_read[i].split())

    print("--- parsing time: ---")
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
