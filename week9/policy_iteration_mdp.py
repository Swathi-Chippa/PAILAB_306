import random

size = 3
goal = (2, 2)
trap = (1, 1)

actions = [(-1,0),(1,0),(0,-1),(0,1)]  # U,D,L,R

# Initialize
V = [[0]*size for _ in range(size)]
policy = [[random.choice(actions) for _ in range(size)] for _ in range(size)]

gamma = 0.9

def next_state(i, j, a):
    ni, nj = i + a[0], j + a[1]
    ni = max(0, min(size-1, ni))
    nj = max(0, min(size-1, nj))
    return ni, nj

def reward(s):
    if s == goal: return 0
    if s == trap: return -10
    return -1

while True:

    # 🔁 Policy Evaluation
    while True:
        delta = 0
        for i in range(size):
            for j in range(size):
                if (i,j) == goal or (i,j) == trap:
                    continue
                ni, nj = next_state(i, j, policy[i][j])
                new_v = reward((ni,nj)) + gamma * V[ni][nj]
                delta = max(delta, abs(V[i][j] - new_v))
                V[i][j] = new_v
        if delta < 0.01:
            break

    # 🔁 Policy Improvement
    stable = True
    for i in range(size):
        for j in range(size):
            if (i,j) == goal or (i,j) == trap:
                continue

            best = None
            best_val = -999

            for a in actions:
                ni, nj = next_state(i, j, a)
                val = reward((ni,nj)) + gamma * V[ni][nj]
                if val > best_val:
                    best_val = val
                    best = a

            if best != policy[i][j]:
                stable = False
            policy[i][j] = best

    if stable:
        break

print("Policy:")
for row in policy:
    print(row)
