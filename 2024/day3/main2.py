import re

mul = re.compile(r'mul\((\d+),(\d+)\)')
dont = re.compile(r"don't\(\)")
do = re.compile(r"do\(\)")


def solution(lines: list[str]):
    ret = 0
    line = ''.join(lines)
    while line:
        mulmatch = mul.search(line)
        dontmatch = dont.search(line)
        domatch = do.search(line)
        if not mulmatch:
            break
        if dontmatch:
            if dontmatch.span(0)[0] < mulmatch.span(0)[0] and (not domatch or (dontmatch.span(0)[0] < domatch.span(0)[0] < mulmatch.span(0)[0])):
                if domatch:
                    line = line[domatch.span(0)[1]:]
                else:
                    break
            else:
                ret += int(mulmatch.group(1)) * int(mulmatch.group(2))
                line = line[mulmatch.span(0)[1]:]
        else:
            ret += int(mulmatch.group(1)) * int(mulmatch.group(2))
            line = line[mulmatch.span(0)[1]:]

    return ret


# data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''.split('\n')

data = open('input.txt', 'r').read().split('\n')

data = [datum for datum in data if datum != '']

print(solution(data))
