import pandas as pd
data = pd.read_csv('SDA_assignment.csv')

missing_values_summary = data.isnull().sum()
total_rows = len(data)
missing_percentage = (missing_values_summary / total_rows) * 100
missing_amount_paid = missing_values_summary['amount_paid']
missing_paid_at = missing_values_summary['paid_at']
missing_percentage_amount_paid = missing_percentage['amount_paid']
missing_percentage_paid_at = missing_percentage['paid_at']

print("Total rows in the dataset:", total_rows)
print("Missing values in 'amount_paid':", missing_amount_paid, "(", missing_percentage_amount_paid, "% )")
print("Missing values in 'paid_at':", missing_paid_at, "(", missing_percentage_paid_at, "% )")
