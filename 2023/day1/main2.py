strnums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
           'seven': 7, 'eight': 8, 'nine': 9}


def substrnum(s):
    for strnum in strnums:
        if s.startswith(strnum):
            return strnums[strnum]
    return 0


def calval(s):
    cv1, cv2 = 0, 0
    for i in range(len(s)):
        if s[i].isdigit():
            cv1 = int(s[i])
            break
        else:
            c = substrnum(s[i:])
            if c != 0:
                cv1 = c
                break

    for ii in range(len(s)):
        i = len(s) - ii - 1
        if s[i].isdigit():
            cv2 = int(s[i])
            break
        else:
            c = substrnum(s[i:])
            if c != 0:
                cv2 = c
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

# data = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
