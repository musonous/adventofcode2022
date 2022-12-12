import sys


def get_common_item(rucksack):
    compartment_len = len(rucksack)
    i = 0
    compartment_2_start = compartment_len // 2
    j = compartment_2_start
    while i < compartment_2_start and j < compartment_len:
        if rucksack[i] == rucksack[j]:
            return rucksack[i]
        j += 1
        if j >= compartment_len:
            i += 1
            j = compartment_2_start
            if i >= compartment_2_start:
                break
    return None


def get_priority(item_type):
    if item_type >= 'a' and item_type <= 'z':
        return ord(item_type) - ord('a') + 1
    if item_type >= 'A' and item_type <= 'Z':
        return ord(item_type) - ord('A') + 27
    return 0


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

with open(filename) as f:
    line = f.readline()
    sum_priorities = 0
    while line:
        item_type = get_common_item(line.strip())
        # print(item_type)
        # print(get_priority(item_type))
        sum_priorities += get_priority(item_type)
        line = f.readline()

print(sum_priorities)
