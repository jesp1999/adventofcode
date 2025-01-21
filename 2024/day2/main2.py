def is_safe(nums):
    safe = True
    inc = nums[0] <= nums[-1]
    for i in range(0, len(nums) - 1):
        diff = abs(nums[i + 1] - nums[i])
        if not (1 <= diff <= 3):
            safe = False
            break
        if inc and nums[i + 1] < nums[i] or (not inc and nums[i + 1] > nums[i]):
            safe = False
            break
    return safe


def solution(lines: list[str]):
    ret = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        safe = is_safe(nums)
        if not safe:
            for i in range(len(nums)):
                safe = is_safe(nums[:i] + nums[i+1:])
                if safe:
                    break
        if safe:
            ret += 1
    return ret


# data = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

data = [datum for datum in data if datum != '']

print(solution(data))
