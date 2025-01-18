import pandas as pd
data = pd.read_csv('SDA_assignment.csv')
paid_leads = data[data['amount_paid'].notnull()]
graduation_year_distribution = paid_leads['graduation_year'].value_counts()
top_5_graduation_years = graduation_year_distribution.head(5)

print("Top 5 Graduation Years of Paid Leads:")
print(top_5_graduation_years)
