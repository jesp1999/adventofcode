def solution(lines: list[str]):
    lines = [line for line in lines if line != '']
    # Mutates input
    ret = 0
    splitlines = [list(line) for line in lines]
    for i in range(len(splitlines)):
        for j in range(len(splitlines[i])):
            if splitlines[i][j] == 'O':
                # Check if can move
                final_i = i
                for test_i in range(i - 1, -1, -1):
                    if splitlines[test_i][j] == '.':
                        final_i = test_i
                    else:
                        break
                if final_i != i:
                    splitlines[final_i][j] = 'O'
                    splitlines[i][j] = '.'
                ret += len(lines) - final_i

    # for i in range(len(splitlines)):
    #     for j in range(len(splitlines[i])):
    #         if splitlines[i][j] == 'O':
    #             print(len(lines) - i)
    print('\n'.join([''.join(l) for l in splitlines]))
    return ret


data = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.split('\n')

# data = '''OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....
# '''.split('\n')

# data = '''OOOO.#.O.. 10
# OO..#....#  9
# OO..O##..O  8
# O..#.OO...  7
# ........#.  6
# ..#....#.#  5
# ..O..#.O.O  4
# ..O.......  3
# #....###..  2
# #....#....  1
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
