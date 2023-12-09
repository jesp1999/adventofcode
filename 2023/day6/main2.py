def solution(lines: list[str]):
    time = int(lines[0].partition(':')[2].replace(' ', ''))
    record_distance = int(lines[1].partition(':')[2].replace(' ', ''))
    ways = 0
    for i in range(time):
        remaining_time = time - i
        speed = i
        if remaining_time * speed > record_distance:
            ways += 1
    return ways


# data = '''Time:      7  15   30
# Distance:  9  40  200
# '''.split('\n')

# data = '''Time:      7  15   30
# Distance:  9  40  200
# '''.split('\n')

# data = '''Time:      71530
# Distance:  940200
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
