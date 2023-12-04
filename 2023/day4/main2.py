def solution(lines: list[str]):
    copies = {}
    lines = [line for line in lines if line != '']
    for line in lines:
        game_number, _, cards = line.partition(':')
        game_number = int(game_number[5:])
        winning_numbers, _, have_numbers = cards.partition('|')
        winning_numbers = [w.strip() for w in winning_numbers.split(' ') if w.strip() != '']
        have_numbers = [w.strip() for w in have_numbers.split(' ') if w.strip() != '']
        copy_count = 0
        for number in winning_numbers:
            if number in have_numbers:
                copy_count += 1
        print([game_number + i + 1 for i in range(copy_count)])
        for i in range(copy_count):
            if game_number + i + 1 not in copies:
                copies[game_number + i + 1] = 0
            copies[game_number + i + 1] += 1 + copies.get(game_number, 0)
    print(copies)
    return sum(copies.values()) + len(lines)


# data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
