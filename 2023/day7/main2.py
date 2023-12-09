card_strengths = {
    'J': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, 'T': 11, 'Q': 12, 'K': 13, 'A': 14
}


def hand_strength(hand_bet):
    hand = hand_bet[0]
    counts = {c: hand.count(c) for c in hand}
    jack_count = 0
    if 'J' in counts:
        jack_count = counts.pop('J')
    counts_vals = tuple(sorted(counts.values()))
    hand_str = 1
    if jack_count == 5 or counts_vals == (5 - jack_count,):
        hand_str = 7  # 5 of a kind
    elif jack_count == 4 or counts_vals == (1, 4 - jack_count):
        hand_str = 6  # 4 of a kind
    elif (jack_count == 3 and counts_vals == (2,)) or counts_vals == (2, 3 - jack_count):
        hand_str = 5  # full house
    elif (jack_count == 3 and counts_vals == (1, 1)) or counts_vals == (1, 1, 3 - jack_count):
        hand_str = 4  # 3 of a kind
    elif (jack_count == 2 and counts_vals == (1, 2)) or counts_vals == (1, 2, 2 - jack_count):
        hand_str = 3  # two pair
    elif (jack_count == 2 and counts_vals == (1, 1, 1)) or counts_vals == (1, 1, 1, 2 - jack_count):
        hand_str = 2  # one pair
    print(f'{hand_bet}={hand_str, *(card_strengths[x] for x in hand)}')
    return hand_str, *(card_strengths[x] for x in hand)


def solution(lines: list[str]):
    hand_bets = [line.split() for line in lines if line != '']
    hand_bets.sort(key=hand_strength)
    print(hand_bets)
    return sum((i + 1) * int(x[1]) for i, x in enumerate(hand_bets))


# data = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
