def possible(game):
    for play in game:
        for pull in play:
            num, _, color = pull.partition(' ')
            num = int(num)
            if color == 'red':
                if num > 12:
                    return False
            elif color == 'green':
                if num > 13:
                    return False
            elif color == 'blue':
                if num > 14:
                    return False
    return True


def solution(lines: list[str]):
    ret = 0
    for line in lines:
        if line == '':
            continue
        split_line = line.split(':')
        game_id = int(split_line[0][5:])
        game = [
            [
                pull.strip() for pull in play.split(', ')
            ] for play in split_line[1].split(';')
        ]
        if possible(game):
            ret += game_id
    return ret


# data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
