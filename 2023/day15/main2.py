def hashmap_algo(input_str, input_map):
    if '-' in input_str:
        label, _, _ = input_str.partition('-')
        label_hash = hash_algo(label)
        idxs_to_remove = []
        if label_hash in input_map:
            for i, pair in enumerate(input_map[label_hash]):
                if pair[0] == label:
                    idxs_to_remove.append(i)
        for idx in idxs_to_remove[::-1]:
            input_map[label_hash].pop(idx)
    elif '=' in input_str:
        label, _, focal_len = input_str.partition('=')
        focal_len = int(focal_len)
        label_hash = hash_algo(label)
        if label_hash not in input_map:
            input_map[label_hash] = []
        idx_to_replace = None
        for i, pair in enumerate(input_map[label_hash]):
            if pair[0] == label:
                idx_to_replace = i
        if idx_to_replace is not None:
            input_map[label_hash][idx_to_replace] = label, focal_len
        else:
            input_map[label_hash].append((label, focal_len))
    else:
        raise NotImplementedError
    return input_map


def hash_algo(input_str) -> int:
    ret = 0
    for c in input_str:
        ret += ord(c)
        ret *= 17
        if ret >= 256:
            ret %= 256
    return ret


def solution(lines: list[str]):
    input_strs = ''.join(lines).replace('\n', '').split(',')
    hash_map = {}
    for i in input_strs:
        hash_map = hashmap_algo(i, hash_map)

    ret = 0
    for label_hash, labels in hash_map.items():
        for i, (label, focal_len) in enumerate(labels):
            ret += (label_hash + 1) * (i + 1) * focal_len
    return ret


# data = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
