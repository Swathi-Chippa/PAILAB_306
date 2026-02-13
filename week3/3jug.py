A_CAP, B_CAP, C_CAP = 8, 5, 3
GOAL = 7

start = (8, 0, 0)

def is_goal(state):
    return GOAL in state

def get_next_states(state):
    a, b, c = state
    states = []

    # A -> B
    pour = min(a, B_CAP - b)
    states.append((a - pour, b + pour, c))

    # A -> C
    pour = min(a, C_CAP - c)
    states.append((a - pour, b, c + pour))

    # B -> A
    pour = min(b, A_CAP - a)
    states.append((a + pour, b - pour, c))

    # B -> C
    pour = min(b, C_CAP - c)
    states.append((a, b - pour, c + pour))

    # C -> A
    pour = min(c, A_CAP - a)
    states.append((a + pour, b, c - pour))

    # C -> B
    pour = min(c, B_CAP - b)
    states.append((a, b + pour, c - pour))

    return states

def dfs_limited(state, path, visited, depth_limit):
    if is_goal(state):
        return path
    if depth_limit == 0:
        return None

    for next_state in get_next_states(state):
        if next_state not in visited:
            visited.add(next_state)
            result = dfs_limited(next_state, path + [next_state], visited, depth_limit - 1)
            if result:
                return result
            visited.remove(next_state)
    return None

def hybrid_ids():
    depth = 0
    while True:
        visited = set()
        visited.add(start)
        path = dfs_limited(start, [start], visited, depth)
        if path:
            return path
        depth += 1


solution_path = hybrid_ids()

print("Solution path (Hybrid BFS+DFS):")
for state in solution_path:
    print(state)
