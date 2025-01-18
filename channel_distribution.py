import pandas as pd
data = pd.read_csv('SDA_assignment.csv')


channel_group_distribution = data['Channel_group'].value_counts()
top_5_channels = channel_group_distribution.head(5)
print("Top 5 Channel Groups Driving Leads:")
print(top_5_channels)
