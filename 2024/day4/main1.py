def solution(lines: list[str]):
    ret = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i >= 3 and j < len(lines[i]) - 3 and lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
                ret += 1
            if j < len(lines[i]) - 3 and lines[i][j] == 'X' and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
                ret += 1
            if i < len(lines) - 3 and j < len(lines[i]) - 3 and lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                ret += 1
            if i < len(lines) - 3 and lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
                ret += 1
            if i < len(lines) - 3 and j >= 3 and lines[i][j] == 'X' and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
                ret += 1
            if j >= 3 and lines[i][j] == 'X' and lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
                ret += 1
            if i >= 3 and j >= 3 and lines[i][j] == 'X' and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
                ret += 1
            if i >= 3 and lines[i][j] == 'X' and lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
                ret += 1
            # check up right
            # check right
            # check down right
            # check down
            ...
        ...
    return ret

# data = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# '''.split('\n')

# data = '''....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

data = [datum for datum in data if datum != '']

print(solution(data))
