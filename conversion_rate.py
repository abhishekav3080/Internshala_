import pandas as pd
data = pd.read_csv('SDA_assignment.csv')
converted_leads = data['amount_paid'].notnull().sum()
total_leads = len(data)

conversion_rate = (converted_leads / total_leads) * 100
print(f"Conversion Rate: {conversion_rate:.2f}%")
