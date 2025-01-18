import pandas as pd
data = pd.read_csv('SDA_assignment.csv')
print("Columns in the dataset:", data.columns)
course_distribution = data['course'].value_counts()  
top_5_courses = course_distribution.head(5)
print("Top 5 Courses by Lead Interest:")
print(top_5_courses)
