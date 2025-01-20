def solution(lines: list[str]):
    n1s, n2s = [], []
    for line in lines:
        n1, _, n2 = line.partition(' ')
        n1s.append(int(n1))
        n2s.append(int(n2))
    n1s.sort()
    n2s.sort()
    return sum([abs(n1s[i] - n2s[i]) for i in range(len(n1s))])


# data = '''3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

data = [datum for datum in data if datum != '']

print(solution(data))
