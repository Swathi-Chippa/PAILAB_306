states = ['Rainy','Sunny']
obs = ['walk','shop','clean']

start = {'Rainy':0.6,'Sunny':0.4}

trans = {
    'Rainy':{'Rainy':0.7,'Sunny':0.3},
    'Sunny':{'Rainy':0.4,'Sunny':0.6}
}

emit = {
    'Rainy':{'walk':0.1,'shop':0.4,'clean':0.5},
    'Sunny':{'walk':0.6,'shop':0.3,'clean':0.1}
}

# Forward Algorithm (simple)
f = {s: start[s]*emit[s][obs[0]] for s in states}

for o in obs[1:]:
    f = {j: sum(f[i]*trans[i][j] for i in states)*emit[j][o] for j in states}

print("Probability of observation sequence:",sum(f.values()))
