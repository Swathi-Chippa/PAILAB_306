from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'Fever': ['Yes','No','Yes','Yes','No','Yes','No','No'],
    'Cough': ['Yes','Yes','No','Yes','No','Yes','No','Yes'],
    'Breathing': ['Yes','No','Yes','No','No','Yes','No','No'],
    'Disease': ['COVID','None','Flu','COVID','None','Flu','None','None']
})

# Define structure
model = DiscreteBayesianNetwork([
    ('Fever', 'Disease'),
    ('Cough', 'Disease'),
    ('Breathing', 'Disease')
])

# Train model
model.fit(data)

# Print CPDs
print("\nConditional Probability Tables (CPDs):")
for cpd in model.get_cpds():
    print(cpd)

# Inference engine
inference = VariableElimination(model)

# Query prediction
result = inference.query(
    variables=['Disease'],
    evidence={'Fever':'Yes', 'Cough':'Yes', 'Breathing':'Yes'}
)

print("\nDisease Prediction:")
print(result)
