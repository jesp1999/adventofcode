from collections import deque


class State:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __eq__(self, other):
        if type(other) is not State:
            return False
        return self.x == other.x and self.y == other.y and self.dx == other.dx and self.dy == other.dy

    def __hash__(self):
        return hash((self.x, self.y, self.dx, self.dy))


def get_next_states(lines: list[str], energized: list[list[bool]], state: State) -> list[State]:
    next_x = state.x + state.dx
    next_y = state.y + state.dy
    if next_x < 0 or next_x >= len(lines[0]) or next_y < 0 or next_y >= len(lines):
        return []
    energized[next_y][next_x] = True
    next_object = lines[next_y][next_x]
    match next_object:
        case '.':
            return [State(next_x, next_y, state.dx, state.dy)]
        case '/':
            return [State(next_x, next_y, -state.dy, -state.dx)]
        case '\\':
            return [State(next_x, next_y, state.dy, state.dx)]
        case '-':
            if state.dx != 0:
                return [State(next_x, next_y, state.dx, 0)]
            if state.dy != 0:
                return [
                    State(next_x, next_y, state.dy, 0),
                    State(next_x, next_y, -state.dy, 0)
                ]
        case '|':
            if state.dx != 0:
                return [
                    State(next_x, next_y, 0, state.dx),
                    State(next_x, next_y, 0, -state.dx)
                ]
            if state.dy != 0:
                return [State(next_x, next_y, 0, state.dy)]


def solution(lines: list[str]):
    lines = [line for line in lines if line != '']
    energized = [[False for _ in line] for line in lines]
    queue = deque()
    queue.append(State(-1, 0, 1, 0))
    # energized[0][0] = True
    visited = set()
    while len(queue) > 0:
        next_states = get_next_states(lines, energized, queue.pop())
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    print('\n'.join([''.join(['#' if c is True else '.' for c in line]) for line in energized]))
    return sum([sum(line) for line in energized])


data = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
'''.split('\n')

# data = '''>|<<<\....
# |v-.\^....
# .v...|->>>
# .v...v^.|.
# .v...v^...
# .v...v^..\
# .v../2\\..
# <->-/vv|..
# .|<<<2-|.\
# .v//.|.v..
# '''.split('\n')

# data = '''######....
# .#...#....
# .#...#####
# .#...##...
# .#...##...
# .#...##...
# .#..####..
# ########..
# .#######..
# .#...#.#..
# '''.split('\n')

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
