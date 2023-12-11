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
        } if p is not None and p not in path_points}
    elif lines[y][x] == '|':
        ret = {(x, y + 1), (x, y - 1)} - path_points
    elif lines[y][x] == 'L':
        ret = {(x + 1, y), (x, y - 1)} - path_points
    elif lines[y][x] == '-':
        ret = {(x + 1, y), (x - 1, y)} - path_points
    elif lines[y][x] == 'J':
        ret = {(x - 1, y), (x, y - 1)} - path_points
    elif lines[y][x] == '7':
        ret = {(x - 1, y), (x, y + 1)} - path_points
    elif lines[y][x] == 'F':
        ret = {(x + 1, y), (x, y + 1)} - path_points
    path_points |= ret
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
    # only include S in calc if it is part of an upper vertical bound
    incl_s_for_area_calc = (
        (start_x, start_y + 1) in points[1]
        or (start_x, start_y - 1) in points[1]
    )
    vert_chars = '|7F' + ('S' if incl_s_for_area_calc else '')
    area = 0
    for y in range(len(lines)):
        flip_count = 0
        for x in range(len(lines[y])):
            if (x, y) in path_points:
                if lines[y][x] in vert_chars:
                    flip_count += 1
            else:
                if flip_count % 2 == 1:
                    area += 1
    return area


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

# data = '''FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
