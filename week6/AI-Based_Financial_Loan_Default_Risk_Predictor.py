from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'Income':      ['High','Low','High','Low','High','Low','High','Low'],
    'Credit':      ['Good','Bad','Good','Bad','Bad','Good','Bad','Good'],
    'Employment':  ['Stable','Unstable','Stable','Unstable','Stable','Unstable','Stable','Unstable'],
    'Default':     ['No','Yes','No','Yes','Yes','No','Yes','No']
})

# Define Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('Income', 'Default'),
    ('Credit', 'Default'),
    ('Employment', 'Default')
])

# Train model
model.fit(data)

# Print CPDs
print("\nCPDs:")
for cpd in model.get_cpds():
    print(cpd)

# Inference engine
inference = VariableElimination(model)

# Query: probability of default
result = inference.query(
    variables=['Default'],
    evidence={'Income': 'Low', 'Credit': 'Bad', 'Employment': 'Unstable'}
)

print("\nLoan Default Risk Prediction:")
print(result)
