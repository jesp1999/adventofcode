import re

mul = re.compile(r'^mul\((\d+),(\d+)\).*')
dont = re.compile(r"^don't\(\)")
do = re.compile(r"^do\(\)")


def solution(lines: list[str]):
    ret = 0
    line = ''.join(lines)
    while line:
        match = mul.search(line)
        if match:
            print(match.groups())
            ret += (int(match.group(1)) * int(match.group(2)))
            line = line[6 + len(match.group(1)) + len(match.group(2)):]
        else:
            line = line[1:]
    return ret


# data = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''.split('\n')

data = open('input.txt', 'r').read().split('\n')

data = [datum for datum in data if datum != '']

print(solution(data))
