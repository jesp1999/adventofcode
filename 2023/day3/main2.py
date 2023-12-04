not_symbols = '.1234567890'


def part_number(line_vicinity, part_number):
    for line in line_vicinity:
        for char in line:
            if char not in not_symbols:
                return part_number
    return 0


def solution(lines: list[str]):
    lines = [line for line in lines if line != '']
    part_coord_map = {}  # map of {line_num: {(part_start, part_end)}}
    gear_coords = []  # list of (line, gear_x)
    ret = 0
    for line_num in range(len(lines)):
        part_number_start, part_number_end = -1, -1
        for j in range(len(lines[line_num])):
            if lines[line_num][j] == '*':
                gear_coords.append((line_num, j))
            if (j == 0 or not lines[line_num][j - 1].isdigit()) and lines[line_num][j].isdigit():
                part_number_start = j
            if (j == (len(lines[line_num]) - 1) or not lines[line_num][j + 1].isdigit()) and lines[line_num][j].isdigit():
                part_number_end = j
            if part_number_end != -1:
                if line_num not in part_coord_map:
                    part_coord_map[line_num] = set()
                part_coord_map[line_num].add((part_number_start, part_number_end))
                part_number_end = -1

    for line_num, gear_coord in gear_coords:
        adjacent_numbers = set()
        for i in range(max(0, line_num - 1), min(len(lines), line_num + 2)):
            for j in range(max(0, gear_coord - 1), min(len(lines[i]), gear_coord + 2)):
                if i == 0 and j == 0:
                    continue
                if i in part_coord_map:
                    for x1, x2 in part_coord_map[i]:
                        if x1 <= j <= x2:
                            adjacent_numbers.add((i, x1, x2))
        if len(adjacent_numbers) == 2:
            ratio_line_num, ratio_num_start, ratio_num_end = adjacent_numbers.pop()
            p1 = int(lines[ratio_line_num][ratio_num_start:ratio_num_end + 1])
            ratio_line_num, ratio_num_start, ratio_num_end = adjacent_numbers.pop()
            p2 = int(lines[ratio_line_num][ratio_num_start:ratio_num_end + 1])
            ret += p1 * p2
    return ret


# data = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
