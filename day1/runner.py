import os
import time
from utility.file_reader import FileReader
from utility.parser import Parser


def part_1(value_list):

    values = []

    for i in range(len(value_list)):

        current_value = 0

        for j in range(len(value_list[i])):
            current_value += value_list[i][j]

        values.append(current_value)

    return max(values)


def part_2(value_list):
    values = []

    for i in range(len(value_list)):

        current_value = 0

        for j in range(len(value_list[i])):
            current_value += value_list[i][j]

        values.append(current_value)

    values.sort(reverse=True)

    return values[0] + values[1] + values[2]


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_reader = FileReader(dir_path + "/input.txt")
    input_read = file_reader.read_file("\n\n")

    value_list = []

    for i in range(len(input_read)):
        parser = Parser(input_read[i].split("\n"))
        value_list.append(parser.convert_to_int())

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
