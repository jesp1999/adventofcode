# TODO: make a more elegant solution. I was tired and used keyboard shortcuts
#  and copy paste to make this solution work in trying to solve the problem
#  in a short enough time to make the leaderboard.

def solution(lines: list[str]):
    ret = 0
    lastret = -1
    coords = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                    ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                    ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                    ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                    ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                    ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                    ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                    ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                    ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j-1] == 'M' and lines[i][j] == 'A' and lines[i-1][j+1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j-1] == 'M' and lines[i][j] == 'A' and lines[i][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j-1] == 'M' and lines[i][j] == 'A' and lines[i+1][j+1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i-1][j] == 'M' and lines[i][j] == 'A' and lines[i+1][j] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i-1][j+1] == 'M' and lines[i][j] == 'A' and lines[i+1][j-1] == 'S':
                #     ret += 1
                # if j >= 1 and j < len(lines[i]) - 1 and lines[i][j+1] == 'M' and lines[i][j] == 'A' and lines[i][j-1] == 'S' :
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == 'M' and lines[i][j] == 'A' and lines[i-1][j-1] == 'S':
                #     ret += 1
                # if i >= 1 and i < len(lines) - 1 and lines[i+1][j] == 'M' and lines[i][j] == 'A' and lines[i-1][j] == 'S':
                #     ret += 1
            # check up right
            # check right
            # check down right
            # check down
            ...
            if ret > lastret != -1:
                coords.append((i, j))
            lastret = ret
        ...
    print(coords)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i, j) in coords:
                print('\033[31m', end='')  # red
            print(lines[i][j] if lines[i][j] != 'X' else ' ', end='')
            if (i, j) in coords:
                print('\033[39m', end='')  # reset
        print('\n', end='')

    return len(coords)

# data = '''
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
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
