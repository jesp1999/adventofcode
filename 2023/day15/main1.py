def hash_algo(input_str) -> int:
    ret = 0
    for c in input_str:
        ret += ord(c)
        ret *= 17
        if ret >= 256:
            ret %= 256
    return ret


def solution(lines: list[str]):
    input_strs = ''.join(lines).replace('\n', '').split(',')
    return sum([hash_algo(i) for i in input_strs])


# data = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
