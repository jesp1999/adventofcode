path_points = set()


def get_adj(lines, x, y):
    global path_points
    ret = set()
    if lines[y][x] == 'S':
        ret = {p for p in {
            check_up(lines, x, y),
            check_down(lines, x, y),
            check_left(lines, x, y),
            check_right(lines, x, y)
        } if p is not None and p not in known_points}
    elif lines[y][x] == '|':
        ret = {(x, y + 1), (x, y - 1)} - known_points
    elif lines[y][x] == 'L':
        ret = {(x + 1, y), (x, y - 1)} - known_points
    elif lines[y][x] == '-':
        ret = {(x + 1, y), (x - 1, y)} - known_points
    elif lines[y][x] == 'J':
        ret = {(x - 1, y), (x, y - 1)} - known_points
    elif lines[y][x] == '7':
        ret = {(x - 1, y), (x, y + 1)} - known_points
    elif lines[y][x] == 'F':
        ret = {(x + 1, y), (x, y + 1)} - known_points
    known_points |= ret
    return ret


def check_left(lines, x, y):
    if x <= 0:
        return None
    return (x - 1, y) if lines[y][x - 1] in '-FL' else None


def check_right(lines, x, y):
    if x >= len(lines[0]) - 1:
        return None
    return (x + 1, y) if lines[y][x + 1] in '-7J' else None


def check_up(lines, x, y):
    if y <= 0:
        return None
    return (x, y - 1) if lines[y - 1][x] in '|F7' else None


def check_down(lines, x, y):
    if y >= len(lines) - 1:
        return None
    return (x, y + 1) if lines[y + 1][x] in '|LJ' else None


def solution(lines: list[str]):
    start_x, start_y = None, None
    lines = [line for line in lines if line != '']
    for i in range(len(lines)):
        if 'S' in lines[i]:
            start_x = i
            start_y = lines[i].index('S')
            break

    points = [{(start_x, start_y)}]
    while len(points[-1]) != 0:
        new_points = set()
        for point in points[-1]:
            new_points |= get_adj(lines, point[0], point[1])
        points.append(new_points)
    points.pop()
    return len(points) - 1


# data = '''.....
# .S-7.
# .|.|.
# .L-J.
# .....
# '''.split('\n')

# data = '''-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF
# '''.split('\n')

# data = '''..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# '''.split('\n')

# data = '''7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
# '''.split('\n')

# data = '''.....
# .S-7.
# .|.|.
# .L-J.
# .....
# '''.split('\n')

# data = '''.....
# .012.
# .1.3.
# .234.
# .....
# '''.split('\n')

data = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''.split('\n')

# data = '''..45.
# .236.
# 01.78
# 14567
# 23...
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
