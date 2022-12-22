import json
import sys


dir_sizes = {}


def calc_dir_size(cur_dir: dict, path):
    assert type(cur_dir) == dict
    sum = 0
    for k, v in cur_dir.items():
        if type(v) == dict:
            sum += calc_dir_size(v, path + k + '/')
        elif type(v) == int:
            sum += v
    dir_sizes.update({
        path: sum,
    })
    return sum


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

# sample_fs = {
#     'a.txt': 10,
#     'dir1': {
#         'b.txt': 12,
#         'dir1_1': {
#             'aa.txt': 6,
#         },
#     },
#     'dir2': {
#         'c.txt': 4,
#     },
# }

with open(filename) as f:
    line = f.readline()
    fs = {}
    dirs = []
    cur_dir = fs
    while line:
        # $ cd /
        # $ cd ..
        # $ ls
        arr = line.strip().split(' ')
        if arr[0] == '$':
            list_started = False
            cmd = arr[1]
            if cmd == 'cd':
                if arr[2] == '/':
                    dirs = []
                    cur_dir = fs
                elif arr[2] == '..':
                    assert len(dirs) > 0
                    if len(dirs) == 1:
                        cur_dir = fs
                    else:
                        cur_dir = dirs[-2]
                    dirs = dirs[:-1]
                else:
                    assert arr[2] in cur_dir and type(cur_dir[arr[2]]) == dict
                    cur_dir = cur_dir[arr[2]]
                    dirs.append(cur_dir)
            elif cmd == 'ls':
                list_started = True
            else:
                assert False
        else:
            assert list_started
            assert len(arr) == 2
            if arr[0] == 'dir':
                cur_dir.update({
                    arr[1]: {},
                })
            else:
                try:
                    size = int(arr[0])
                except:
                    assert False
                cur_dir.update({
                    arr[1]: size,
                })
        line = f.readline()
    print(json.dumps(fs, indent=2))

    print(calc_dir_size(fs, '/'))

    print(json.dumps(dir_sizes, indent=2))

    c = 0
    s = 0
    for k, v in dir_sizes.items():
        if v <= 100000:
            c += 1
            s += v

    print(c, s)

    free_space = 70000000 - dir_sizes['/']
    needed_space = 30000000 - free_space
    print(free_space, needed_space)

    choosed_dir_size = 0
    choosed_dir_path = None
    for k, v in dir_sizes.items():
        if v >= needed_space:
            if choosed_dir_size == 0 or v < choosed_dir_size:
                choosed_dir_size = v
                choosed_dir_path = k

    print(choosed_dir_path, choosed_dir_size)

