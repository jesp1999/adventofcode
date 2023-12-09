def solution(lines: list[str]):
    times = [int(s) for s in lines[0].partition(':')[2].strip().split()]
    record_distances = [int(s) for s in lines[1].partition(':')[2].strip().split()]
    print(times)
    print(record_distances)
    ret = 1
    for time, record_distance in zip(times, record_distances):
        ways = 0
        for i in range(time):
            remaining_time = time - i
            speed = i
            if remaining_time * speed > record_distance:
                ways += 1
        ret *= ways
    return ret

#
# data = '''Time:      7  15   30
# Distance:  9  40  200
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
