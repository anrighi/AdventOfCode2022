import os
import time
from utility.file_reader import FileReader


def part_1(value_list):

    last_four = []

    for i in range(len(value_list)):
        if len(last_four) < 4:
            last_four.append(value_list[i])
        elif len(last_four) == len(set(last_four)):
            return i
        else:
            last_four.pop(0)
            last_four.append(value_list[i])

    return -1


def part_2(value_list):

    last_fourteen = []

    for i in range(len(value_list)):
        if len(last_fourteen) < 14:
            last_fourteen.append(value_list[i])
        elif len(last_fourteen) == len(set(last_fourteen)):
            return i
        else:
            last_fourteen.pop(0)
            last_fourteen.append(value_list[i])

    return -1


def main():

    start_time = time.time()
    print("--- day6 ---")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_reader = FileReader(dir_path + "/input.txt")
    input_read = file_reader.read_file()
    input_read = [*input_read[0]]

    print("--- parsing time: ---")
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 1: ", part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
