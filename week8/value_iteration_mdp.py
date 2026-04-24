import numpy as np

# Grid size and special states
size = 3
goal = (2, 2)
trap = (1, 1)

actions = [(-1,0),(1,0),(0,-1),(0,1)]  # UP, DOWN, LEFT, RIGHT

# Initialize values
V = np.zeros((size, size))

gamma = 0.9
epsilon = 0.01

def get_next(i, j, a):
    ni, nj = i + a[0], j + a[1]
    ni = max(0, min(size-1, ni))
    nj = max(0, min(size-1, nj))
    return ni, nj

def reward(s):
    if s == goal:
        return 0
    if s == trap:
        return -10
    return -1

# Value Iteration
while True:
    delta = 0
    newV = V.copy()

    for i in range(size):
        for j in range(size):
            if (i,j) == goal or (i,j) == trap:
                continue

            values = []
            for a in actions:
                ni, nj = get_next(i, j, a)
                values.append(reward((ni,nj)) + gamma * V[ni][nj])

            newV[i][j] = max(values)
            delta = max(delta, abs(V[i][j] - newV[i][j]))

    V = newV
    if delta < epsilon:
        break

print("Optimal Values:\n", V)
