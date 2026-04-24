# Policy Iteration for Warehouse Robot Scheduling

states = ["Idle", "Working"]
actions = ["Work", "Charge"]
gamma = 0.9

# Initial policy and values
policy = {s: "Work" for s in states}
V = {s: 0 for s in states}

# Policy Iteration
for _ in range(10):

    # Policy Evaluation
    for s in states:
        V[s] = 5 + gamma * V[s]

    # Policy Improvement
    for s in states:
        if V[s] > 2:
            policy[s] = "Work"
        else:
            policy[s] = "Charge"

# Output
print("Optimal Warehouse Robot Policy:", policy)
