import os
import time
from utility.file_reader import FileReader


def part_1(value_list):

    pairs = 0

    for i in range(len(value_list)):

        assignment_1 = value_list[i][0].split("-")
        assignment_1 = [int(x) for x in assignment_1]

        assignment_2 = value_list[i][1].split("-")
        assignment_2 = [int(x) for x in assignment_2]

        if assignment_1[0] <= assignment_2[0] and assignment_1[1] >= assignment_2[1] or assignment_2[0] <= assignment_1[0] and assignment_2[1] >= assignment_1[1]:
            pairs += 1

    return pairs


def part_2(value_list):
    pairs = 0

    for i in range(len(value_list)):

        assignment_1 = value_list[i][0].split("-")
        assignment_1 = [int(x) for x in assignment_1]

        assignment_2 = value_list[i][1].split("-")
        assignment_2 = [int(x) for x in assignment_2]

        if assignment_1[0] <= assignment_2[0] and assignment_1[1] >= assignment_2[1] or assignment_2[0] <= assignment_1[0] and assignment_2[1] >= assignment_1[1] or assignment_1[0] <= assignment_2[0] and assignment_1[1] >= assignment_2[0] or assignment_2[0] <= assignment_1[0] and assignment_2[1] >= assignment_1[0]:
            pairs += 1

    return pairs


def main():

    start_time = time.time()
    print("--- day4 ---")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_reader = FileReader(dir_path + "/input.txt")
    input_read = file_reader.read_file("\n")

    input_read = [x.split(",") for x in input_read]

    print("--- parsing time: ---")
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 1: ", part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
