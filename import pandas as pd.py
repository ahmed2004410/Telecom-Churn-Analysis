import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        # Basic Logic
        tenure = random.randint(0, 72)
        monthly = round(random.uniform(20.0, 118.0), 2)
        total = round(tenure * monthly, 2)
        churn_label = random.choice(['Yes', 'No'])
        churn_val = 1 if churn_label == 'Yes' else 0
        
        # Row Structure
        row = {
            'customer_id': fake.bothify(text='####-????').upper(),
            'gender': random.choice(['Male', 'Female']),
            'senior_citizen': random.choice(['Yes', 'No']),
            'partner': random.choice(['Yes', 'No']),
            'dependents': random.choice(['Yes', 'No']),
            'count': 1,
            'country': 'United States',
            'state': 'California',
            'city': fake.city(),
            'zip_code': fake.zipcode(),
            'lat_long': f"{fake.latitude()}, {fake.longitude()}",
            'latitude': float(fake.latitude()),
            'longitude': float(fake.longitude()),
            'phone_service': random.choice(['Yes', 'No']),
            'multiple_lines': random.choice(['Yes', 'No', 'No phone service']),
            'internet_service': random.choice(['DSL', 'Fiber optic', 'No']),
            'online_security': random.choice(['Yes', 'No', 'No internet service']),
            'online_backup': random.choice(['Yes', 'No', 'No internet service']),
            'device_protection': random.choice(['Yes', 'No', 'No internet service']),
            'tech_support': random.choice(['Yes', 'No', 'No internet service']),
            'streaming_tv': random.choice(['Yes', 'No', 'No internet service']),
            'streaming_movies': random.choice(['Yes', 'No', 'No internet service']),
            'paperless_billing': random.choice(['Yes', 'No']),
            'payment_method': random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card']),
            'contract': random.choice(['Month-to-month', 'One year', 'Two year']),
            'tenure_months': tenure,
            'monthly_charges': monthly,
            'total_charges': total,
            'churn_label': churn_label,
            'churn_value': churn_val,
            'churn_score': random.randint(0, 100),
            'cltv': random.randint(2000, 8000),
            'churn_reason': random.choice(['Competitor made better offer', 'Price too high', 'Moved', '']) if churn_label == 'Yes' else ''
        }
        data.append(row)
    
    return pd.DataFrame(data)

# Generate 1000 rows (Change number as needed)
df = generate_data(10000)

# Save to CSV
df.to_csv(f'D:/telco_data.csv', index=False)
print("Done! File saved as telco_data.csv")