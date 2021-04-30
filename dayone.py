def readfile():
    with open("inputs/1.txt") as f:
        content = [int(x.strip()) for x in f.readlines()]
    return content


def get2020pair(arr, _min) -> (int, int):
    prune = [x for x in arr if x + _min <= 2020]
    values = [(i, j) for i in arr for j in arr if i + j == 2020]
    return values[0]


def get2020triad(arr, _min) -> (int, int, int):
    prune = [x for x in arr if x + _min <= 2020]
    values = [(i, j, x) for i in arr for j in arr for x in arr if i + j + x == 2020]
    return values[0]


def solve():
    arr = readfile()
    x, y = get2020pair(arr, min(arr))
    x1, y1, z = get2020triad(arr, min(arr))
    print(f'[Advent of Code | Day 1 (Part 1)] Solution : {(x * y)}')
    print(f'[Advent of Code | Day 1 (Part 2)] Solution : {(x1 * y1 * z)}')
