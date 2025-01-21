def match_rules(update, rules):
    for start, end in rules:
        if start in update and end in update:
            if update.index(start) > update.index(end):
                return False
    return True


def solution(lines: list[str]):
    ret = 0
    section = 0
    rules = []
    updates = []
    for line in lines:
        if line == '':
            section += 1
            continue
        if section == 0:
            rules.append(tuple(line.split('|')))
        elif section == 1:
            updates.append(line.split(','))

    print(rules)
    print(updates)
    for update in updates:
        if match_rules(update, rules):
            ret += int(update[(len(update) - 1) // 2])
    ...
    return ret


data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''.split('\n')

# data = open('input.txt', 'r').read().split('\n')

data = [datum for datum in data][:-1]

print(solution(data))
