# Value Iteration for Traffic Signal Control

states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9

# Rewards for each state
reward = {
    "Low": 10,
    "Medium": 5,
    "High": -10
}

# Initialize state values
V = {s: 0 for s in states}

# Value Iteration
for _ in range(20):  # fixed iterations
    for s in states:
        V[s] = max(reward[s] + gamma * V[s] for a in actions)

# Output
print("Optimal State Values for Traffic Control:", V)
