import sys


#         [H]     [W] [B]
#     [D] [B]     [L] [G] [N]
# [P] [J] [T]     [M] [R] [D]
# [V] [F] [V]     [F] [Z] [B]     [C]
# [Z] [V] [S]     [G] [H] [C] [Q] [R]
# [W] [W] [L] [J] [B] [V] [P] [B] [Z]
# [D] [S] [M] [S] [Z] [W] [J] [T] [G]
# [T] [L] [Z] [R] [C] [Q] [V] [P] [H]
#  1   2   3   4   5   6   7   8   9

stack = [
    ['T', 'D', 'W', 'Z', 'V', 'P'],
    ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    ['R', 'S', 'J'],
    ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    ['P', 'T', 'B', 'Q'],
    ['H', 'G', 'Z', 'R', 'C'],
]


def move_stack(c, f, t):
    global stack
    print(c, f, t)
    # print(stack)
    for s in stack:
        print(s)
    assert len(stack[f-1]) >= c
    cargo = stack[f-1][-c:]
    stack[f-1] = stack[f-1][:-c]
    if stack[f-1] is None:
        stack[f-1] = []
    # cargo = reversed(cargo)
    for c in cargo:
        stack[t-1].append(c)


def parse_line(line: str):
    arr = line.split(' ')
    assert len(arr) == 6
    return int(arr[1]), int(arr[3]), int(arr[5])


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

with open(filename) as f:
    line = f.readline()
    num_fully_contain = 0
    num_overlap = 0
    while line:
        _count, _from, _to = parse_line(line.strip())
        move_stack(_count, _from, _to)
        line = f.readline()

    print('=========')
    for s in stack:
        print(s)
    for s in stack:
        print(s[-1], end='')
    print()
