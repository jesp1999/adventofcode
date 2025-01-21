def solution(lines: list[str]):
    ret = 0
    n1s, n2s = [], []
    for line in lines:
        n1, _, n2 = line.partition(' ')
        n1s.append(int(n1))
        n2s.append(int(n2))
    for i in range(len(n1s)):
        ret += n1s[i] * n2s.count(n1s[i])
    return ret


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
