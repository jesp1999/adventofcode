def calval(s):
    cv1, cv2 = 0, 0
    for i in range(len(s)):
        if s[i].isdigit():
            cv1 = int(s[i])
            break

    for ii in range(len(s)):
        i = len(s) - ii - 1
        if s[i].isdigit():
            cv2 = int(s[i])
            break
    return cv1 * 10 + cv2


def solution(lines: list[str]):
    ret = 0
    for line in lines:
        c = calval(line)
        ret += c
    return ret


# data = '''1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
