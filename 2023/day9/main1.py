def solution(lines: list[str]):
    ret = 0
    for line in lines:
        if line == '':
            continue
        diffs = [[int(s) for s in line.split()]]
        while not all(val == 0 for val in diffs[-1]):
            diff = []
            for i in range(len(diffs[-1]) - 1):
                diff.append(diffs[-1][i + 1] - diffs[-1][i])
            diffs.append(diff)
        diffs[-1].append(diffs[-1][-1])
        for i in range(len(diffs) - 1):
            diffs[-2 - i].append(diffs[-2 - i][-1] + diffs[-1 - i][-1])
        ret += diffs[0][-1]
    return ret


# data = '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
