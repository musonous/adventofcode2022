import sys


def is_fully_contain(section_1, section_2):
    if ((int(section_1[0]) <= int(section_2[0]) and int(section_1[1]) >= int(section_2[1])) or
        (int(section_2[0]) <= int(section_1[0]) and int(section_2[1]) >= int(section_1[1]))):
        return True
    return False


def is_overlap(section_1, section_2):
    if ((int(section_1[0]) <= int(section_2[0]) and int(section_1[1]) >= int(section_2[0])) or
        (int(section_2[0]) <= int(section_1[0]) and int(section_2[1]) >= int(section_1[0]))):
        return True
    return False


def parse_section(line: str):
    arr = line.split(',')
    assert len(arr) == 2
    section_1 = arr[0].split('-')
    assert len(section_1) == 2
    section_2 = arr[1].split('-')
    assert len(section_2) == 2
    return section_1, section_2


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

with open(filename) as f:
    line = f.readline()
    num_fully_contain = 0
    num_overlap = 0
    while line:
        section_1, section_2 = parse_section(line.strip())
        if is_fully_contain(section_1, section_2):
            num_fully_contain += 1
        if is_overlap(section_1, section_2):
            num_overlap += 1
        line = f.readline()

    print(num_fully_contain)
    print(num_overlap)
