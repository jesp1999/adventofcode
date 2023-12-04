not_symbols = '.1234567890'


def part_number(line_vicinity, part_number):
    for line in line_vicinity:
        for char in line:
            if char not in not_symbols:
                return part_number
    return 0


def solution(lines: list[str]):
    lines = [line for line in lines if line != '']
    part_coords = []  # list of (line, part_start, part_end)
    ret = 0
    for line_num in range(len(lines)):
        part_number_start, part_number_end = -1, -1
        for j in range(len(lines[line_num])):
            if (j == 0 or not lines[line_num][j - 1].isdigit()) and lines[line_num][j].isdigit():
                part_number_start = j
            if (j == (len(lines[line_num]) - 1) or not lines[line_num][j + 1].isdigit()) and lines[line_num][j].isdigit():
                part_number_end = j
            if part_number_end != -1:
                part_coords.append((line_num, part_number_start, part_number_end))
                part_number_end = -1
    for line_num, part_number_start, part_number_end in part_coords:
        p = part_number(
            [line[max(0, part_number_start - 1): part_number_end + 2]
             for line in lines[max(0, line_num - 1): line_num + 2]],
            int(lines[line_num][part_number_start:part_number_end + 1])
        )
        if p != 0:
            print((line_num, part_number_start))
        ret += p
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
