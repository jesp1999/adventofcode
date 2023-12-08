def fn(x, range_offset_map):
    for a, b in range_offset_map:
        if a <= x < b:
            return x + range_offset_map[(a, b)]
    return x


def solution(lines: list[str]):
    stuff = '\n'.join(lines).split('\n\n')
    maps = []
    for raw_map in stuff[1:]:
        raw_rows = raw_map.partition(':')[2].strip().split('\n')
        range_offset_map = {}
        for raw_row in raw_rows:
            nums = [int(s) for s in raw_row.split()]
            dst = nums[0]
            src = nums[1]
            rng = nums[2]
            range_offset_map[(src, src + rng)] = dst - src
        maps.append(range_offset_map)

    seeds = [int(s) for s in stuff[0].partition(':')[2].strip().split()]
    mapped_seeds = []
    for seed in seeds:
        for range_offset_map in maps:
            seed = fn(seed, range_offset_map)
        mapped_seeds.append(seed)
    return min(mapped_seeds)


# data = '''seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4
# '''.split('\n')

# data = '''seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
