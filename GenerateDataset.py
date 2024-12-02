import pandas as pd
import numpy as np

# Define the number of rows
num_rows = 1000

# Generate random data
np.random.seed(42)
customer_ids = [f'{i:04d}-{np.random.choice(["ABCD", "WXYZ", "LMNO", "PQRS", "TUV"])[:4]}' for i in range(num_rows)]

genders = np.random.choice(['Male', 'Female'], num_rows)
senior_citizens = np.random.choice(['Yes', 'No'], num_rows)
partners = np.random.choice(['Yes', 'No'], num_rows)
dependents = np.random.choice(['Yes', 'No'], num_rows)
tenures = np.random.randint(1, 72, num_rows)
phone_services = np.random.choice(['Yes', 'No'], num_rows)
internet_services = np.random.choice(['DSL', 'Fiber Optic', 'No'], num_rows)
monthly_charges = np.round(np.random.uniform(20, 120, num_rows), 2)
total_charges = np.round(monthly_charges * tenures, 2)
churn = np.random.choice(['Yes', 'No'], num_rows)
contract_types = np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], num_rows)

# Create a DataFrame
data = {
    'CustomerID': customer_ids,
    'Gender': genders,
    'SeniorCitizen': senior_citizens,
    'Partner': partners,
    'Dependents': dependents,
    'Tenure (months)': tenures,
    'PhoneService': phone_services,
    'InternetService': internet_services,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'Churn': churn,
    'Contract Type': contract_types
}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('telecom_customer_details.csv', index=False)
