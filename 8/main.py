import json
import sys


def calc_scenic_score(map, i, j):
    if i == 0 or i == len(map) - 1 or j == 0 or j == len(map[i]) - 1:
        return 0

    height = map[i][j]

    viewing_distance_left = 0
    for k in range(j-1, -1, -1):
        viewing_distance_left += 1
        if map[i][k] >= height:
            break

    viewing_distance_right = 0
    for k in range(j+1, len(map[i])):
        viewing_distance_right += 1
        if map[i][k] >= height:
            break

    viewing_distance_top = 0
    for k in range(i-1, -1, -1):
        viewing_distance_top += 1
        if map[k][j] >= height:
            break

    viewing_distance_bottom = 0
    for k in range(i+1, len(map)):
        viewing_distance_bottom += 1
        if map[k][j] >= height:
            break

    return viewing_distance_left * viewing_distance_right * viewing_distance_top * viewing_distance_bottom


def is_visible(map, i, j):
    if i == 0 or i == len(map) - 1 or j == 0 or j == len(map[i]) - 1:
        return True

    height = map[i][j]

    visible_left = True
    for k in range(0, j):
        if map[i][k] >= height:
            visible_left = False
            break
    if visible_left:
        return True

    visible_right = True
    for k in range(j+1, len(map[i])):
        if map[i][k] >= height:
            visible_right = False
            break
    if visible_right:
        return True

    visible_top = True
    for k in range(0, i):
        if map[k][j] >= height:
            visible_top = False
            break
    if visible_top:
        return True

    visible_bottom = True
    for k in range(i+1, len(map)):
        if map[k][j] >= height:
            visible_bottom = False
            break
    if visible_bottom:
        return True

    return False


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

with open(filename) as f:
    line = f.readline()
    map = []
    while line:
        row = []
        for c in line.strip():
            row.append(int(c))
        map.append(row)
        line = f.readline()

    num_visible = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if is_visible(map, i, j):
                num_visible += 1
    print(num_visible)

    max_scenic_score = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            ss = calc_scenic_score(map, i, j)
            if ss > max_scenic_score:
                max_scenic_score = ss
    print(max_scenic_score)
