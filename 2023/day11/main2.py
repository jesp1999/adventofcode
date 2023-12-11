def expand_space(lines: list[str], ):
    ...


def solution(lines: list[str]):
    lines = [line for line in lines if line != '']
    ret = 0
    bigger_rows = []
    no_galaxy_in_cols = [True] * len(lines)
    galaxy_coords = []
    for i in range(len(lines)):
        no_galaxy_in_row = True
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                no_galaxy_in_row = False
                no_galaxy_in_cols[j] = False
                galaxy_coords.append((i, j))
        if no_galaxy_in_row:
            bigger_rows.append(i)
    bigger_cols = [i for i in range(len(no_galaxy_in_cols)) if no_galaxy_in_cols[i]]
    for i, (g1_i, g1_j) in enumerate(galaxy_coords):
        for j, (g2_i, g2_j) in enumerate(galaxy_coords[i:]):
            r = 0
            if g1_i == g2_i and g1_j == g2_j:
                continue
            i_range = range(min(g1_i, g2_i) + 1, max(g1_i, g2_i))
            j_range = range(min(g1_j, g2_j) + 1, max(g1_j, g2_j))
            if g1_i != g2_i:
                r += 1
            if g1_j != g2_j:
                r += 1
            for step_i in i_range:
                r += 1000000 if step_i in bigger_rows else 1
            for step_j in j_range:
                r += 1000000 if step_j in bigger_cols else 1
            ret += r
    return ret


data = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''.split('\n')

# data = '''   v  v  v
#  ...#......
#  .......#..
#  #.........
# >..........<
#  ......#...
#  .#........
#  .........#
# >..........<
#  .......#..
#  #...#.....
#    ^  ^  ^
# '''.split('\n')

# data = '''....#........
# .........#...
# #............
# .............
# .............
# ........#....
# .#...........
# ............#
# .............
# .............
# .........#...
# #....#.......
# '''.split('\n')

# data = '''....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# ............6
# .............
# .............
# .........7...
# 8....9.......
# '''.split('\n')

# data = '''....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# .##.........6
# ..##.........
# ...##........
# ....##...7...
# 8....9.......
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
