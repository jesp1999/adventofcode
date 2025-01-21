from graphlib import TopologicalSorter
import pyperclip as pc


def match_rules(update, rules):
    for start, end in rules:
        if start in update and end in update:
            if update.index(start) > update.index(end):
                return False
    return True

def reorder(update, rules):
    graph = {}
    for start, end in rules:
        if start not in update:
            continue
        if start not in graph:
            graph[start] = set()
        graph[start].add(end)
    topo_sorted = list(TopologicalSorter(graph).static_order())[::-1]
    mp = {n: i for i, n in enumerate(topo_sorted)}
    return list(sorted(update, key=lambda n: mp[n]))


def solution(lines: list[str]):
    ret = 0
    rules = []
    updates = []
    for line in lines:
        if '|' in line:
            rules.append(tuple(line.split('|')))
        elif ',' in line:
            updates.append(line.split(','))

    bad_updates = []
    for update in updates:
        if not match_rules(update, rules):
            bad_updates.append(update)

    reordered_updates = []
    for update in bad_updates:
        reordered_update = reorder(update, rules)
        reordered_updates.append(reordered_update)
        ret += int(reordered_update[(len(reordered_update)-1) // 2])
    return ret


# data = '''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# '''.split('\n')

data = open('../day5/input.txt', 'r').read().split('\n')

s = solution(data)
print(s)
pc.copy(s)
