import pandas as pd
data = pd.read_csv('SDA_assignment.csv')



paid_leads_count = data[data['amount_paid'].notnull()].shape[0]
free_leads_count = data[data['amount_paid'].isnull()].shape[0]


print(f"Paid Leads: {paid_leads_count}")
print(f"Free Leads: {free_leads_count}")

