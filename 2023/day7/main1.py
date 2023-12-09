card_strengths = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}


def hand_strength(hand_bet):
    hand = hand_bet[0]
    counts = {c: hand.count(c) for c in hand}
    counts_vals = tuple(sorted(counts.values()))
    hand_str = 1
    if counts_vals == (5,):
        hand_str = 7  # 5 of a kind
    elif counts_vals == (1, 4):
        hand_str = 6  # 4 of a kind
    elif counts_vals == (2, 3):
        hand_str = 5  # full house
    elif counts_vals == (1, 1, 3):
        hand_str = 4  # 3 of a kind
    elif counts_vals == (1, 2, 2):
        hand_str = 3  # two pair
    elif counts_vals == (1, 1, 1, 2):
        hand_str = 2  # one pair
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
# QQQJA 483'''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
