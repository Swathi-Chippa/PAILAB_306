from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# Balanced dataset (IMPORTANT)
data = pd.DataFrame({
    'Rain': ['No','No','Yes','Yes','No','Yes','Yes','No'],
    'TrafficJam': ['Yes','No','Yes','No','Yes','No','Yes','No'],
    'ArriveLate': ['No','Yes','Yes','No','No','Yes','Yes','No']
})

# Define structure
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# Train model
model.fit(data)

# Print CPDs
print("\nConditional Probability Tables (CPDs):")
for cpd in model.get_cpds():
    print(cpd)

# Inference
inference = VariableElimination(model)

result = inference.query(
    variables=['ArriveLate'],
    evidence={'Rain': 'Yes'}
)

print("\nInference Result:")
print(result)
