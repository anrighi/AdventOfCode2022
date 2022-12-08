import os
import time
import re
import copy
from utility.file_reader import FileReader

stacks_init = {
    1: ["W", "B", "D", "N", "C", "F", "J"],
    2: ["P", "Z", "V", "Q", "L", "S", "T"],
    3: ["P", "Z", "B", "G", "J", "T"],
    4: ["D", "T", "L", "J", "Z", "B", "H", "C"],
    5: ["G", "V", "B", "J", "S"],
    6: ["P", "S", "Q"],
    7: ["B", "V", "D", "F", "L", "M", "P", "N"],
    8: ["P", "S", "M", "F", "B", "D", "L", "R"],
    9: ["V", "D", "T", "R"]
}


def part_1(value_list):

    stacks = copy.deepcopy(stacks_init)

    for i in range(len(value_list)):

        search = re.search("move (\d+) from (\d+) to (\d+)", value_list[i])

        if search:
            crates_number = int(search.group(1))
            from_stack = int(search.group(2))
            to_stack = int(search.group(3))

            for j in range(crates_number):
                moved_crate = stacks[from_stack].pop()
                stacks[to_stack].append(moved_crate)

    return_string = ""

    for stack in stacks:
        return_string += "".join(stacks[stack][-1])

    return return_string


def part_2(value_list):

    stacks = copy.deepcopy(stacks_init)

    for i in range(len(value_list)):

        search = re.search("move (\d+) from (\d+) to (\d+)", value_list[i])

        if search:
            crates_number = int(search.group(1))
            from_stack = int(search.group(2))
            to_stack = int(search.group(3))

            print(value_list[i])
            print(stacks[from_stack], stacks[to_stack])

            moved_crate = stacks[from_stack][-crates_number:]
            print("moved: ", moved_crate)
            stacks[from_stack] = stacks[from_stack][:len(
                stacks[from_stack]) - crates_number]
            stacks[to_stack] = stacks[to_stack] + moved_crate

            print(stacks[from_stack], stacks[to_stack])

    return_string = ""

    for stack in stacks:
        return_string += "".join(stacks[stack][-1])

    return return_string


def main():

    start_time = time.time()
    print("--- day5 ---")

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
