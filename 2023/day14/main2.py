from copy import deepcopy


def total_north_beam_load(splitlines: list[list[str]]) -> int:
    load = 0
    for i in range(len(splitlines)):
        for j in range(len(splitlines[i])):
            if splitlines[i][j] == 'O':
                load += len(splitlines) - i
    return load


def full_cycle(splitlines: list[list[str]]) -> list[list[str]]:
    splitlines = deepcopy(splitlines)
    # North
    for i in range(len(splitlines)):
        for j in range(len(splitlines[i])):
            if splitlines[i][j] == 'O':
                final_i = i
                for test_i in range(i - 1, -1, -1):
                    if splitlines[test_i][j] == '.':
                        final_i = test_i
                    else:
                        break
                if final_i != i:
                    splitlines[final_i][j] = 'O'
                    splitlines[i][j] = '.'

    # West
    for i in range(len(splitlines)):
        for j in range(len(splitlines[i])):
            if splitlines[i][j] == 'O':
                final_j = j
                for test_j in range(j - 1, -1, -1):
                    if splitlines[i][test_j] == '.':
                        final_j = test_j
                    else:
                        break
                if final_j != j:
                    splitlines[i][final_j] = 'O'
                    splitlines[i][j] = '.'

    # South
    for i in range(len(splitlines) - 1, -1, -1):
        for j in range(len(splitlines[i])):
            if splitlines[i][j] == 'O':
                final_i = i
                for test_i in range(i + 1, len(splitlines)):
                    if splitlines[test_i][j] == '.':
                        final_i = test_i
                    else:
                        break
                if final_i != i:
                    splitlines[final_i][j] = 'O'
                    splitlines[i][j] = '.'

    # East
    for i in range(len(splitlines)):
        for j in range(len(splitlines[i]) - 1, -1, -1):
            if splitlines[i][j] == 'O':
                final_j = j
                for test_j in range(j + 1, len(splitlines[0])):
                    if splitlines[i][test_j] == '.':
                        final_j = test_j
                    else:
                        break
                if final_j != j:
                    splitlines[i][final_j] = 'O'
                    splitlines[i][j] = '.'
    return splitlines


def solution(lines: list[str]):
    splitlines = [list(line) for line in lines if line != '']
    snapshot_weight_map = {}
    snapshots = []
    for cycle in range(1000000000):
        snapshots.append(hash(''.join([''.join(l) for l in splitlines])))
        if snapshots[-1] in snapshot_weight_map:
            # Cycle detected [ 232, 2, 4, 5, 4, 2] (1000 - i) % cycle_duration
            #                    0, 1, 2, 3, 4, 5
            #                       1           5
            #
            cycle_start = snapshots.index(snapshots[-1])
            cycle_duration = len(snapshots) - 1 - cycle_start
            final_snapshot = snapshots[
                cycle_start + ((1000000000 - cycle_start) % cycle_duration)
            ]
            return snapshot_weight_map[final_snapshot]

        snapshot_weight_map[snapshots[-1]] = total_north_beam_load(splitlines)

        splitlines = full_cycle(splitlines)


# data = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
