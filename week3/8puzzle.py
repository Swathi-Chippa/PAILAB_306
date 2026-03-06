import heapq

# Goal State
GOAL = ((1,2,3),
        (4,5,6),
        (7,8,0))

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_row = (value - 1) // 3
                goal_col = (value - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    row, col = find_blank(state)

    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    for dr, dc in moves:
        new_r = row + dr
        new_c = col + dc

        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = [list(r) for r in state]
            new_state[row][col], new_state[new_r][new_c] = \
                new_state[new_r][new_c], new_state[row][col]

            neighbors.append(tuple(tuple(r) for r in new_state))

    return neighbors


def greedy_search(start):

    open_list = []
    heapq.heappush(open_list, (heuristic(start), start, [start]))

    visited = set()

    while open_list:
        h, current, path = heapq.heappop(open_list)

        if current == GOAL:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_list,
                               (heuristic(neighbor),
                                neighbor,
                                path + [neighbor]))

    return None


start_state = ((1,2,3),
               (4,0,6),
               (7,5,8))

solution = greedy_search(start_state)

if solution:
    print("Solved in", len(solution)-1, "moves\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")

