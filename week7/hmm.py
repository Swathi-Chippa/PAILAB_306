states = ['I', 'N', 'D']  # Interested, Neutral, Disengaged
obs = ['high', 'medium', 'low']

start = {'I':0.5, 'N':0.3, 'D':0.2}

trans = {
    'I':{'I':0.6,'N':0.3,'D':0.1},
    'N':{'I':0.2,'N':0.5,'D':0.3},
    'D':{'I':0.1,'N':0.3,'D':0.6}
}

emit = {
    'I':{'high':0.7,'medium':0.2,'low':0.1},
    'N':{'high':0.3,'medium':0.4,'low':0.3},
    'D':{'high':0.1,'medium':0.3,'low':0.6}
}

def fwd():
    f = {s: start[s]*emit[s][obs[0]] for s in states}
    for t in obs[1:]:
        f = {j: sum(f[i]*trans[i][j] for i in states)*emit[j][t] for j in states}
    return sum(f.values())

print("Probability of observation sequence:", fwd())
