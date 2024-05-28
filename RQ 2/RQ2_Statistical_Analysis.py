import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#This script is written to create a correlation matrix for the data collected for perceived productivity of software engineers

# Load the Excel file to examine the content
file_path = "../Effects of Remote Work on the Productivity of Software Engineers (Responses).xlsx"
data = pd.read_excel(file_path)
data.head()


# Prepare a DataFrame for correlation analysis by extracting relevant variables
data_correlation = data[[
    'If applicable: On average, how many hours do you work per day Onsite ?',
    'If applicable: On average, how many hours do you work per day Remotely?',
    'If applicable: How many work-related tasks do you complete on an average day Onsite? This can be coding tasks, meetings, design etc. ',
    'If applicable: How many work-related tasks do you complete on an average day Remotely? This can be coding tasks, meetings, design etc. ',
    'On a scale of 1 (much less) to 5 (much more), rate the level of support you receive from your company while working remotely.',
    'How frequently do you experience technical issues that impact your productivity when working remotely?',
    'On a scale from 1 (much less productive) to 5 (much more productive), how do you rate your productivity working remotely compared to onsite? '
]].copy()

data_correlation.rename(columns={
    'If applicable: On average, how many hours do you work per day Onsite ?': 'Hours_Onsite',
    'If applicable: On average, how many hours do you work per day Remotely?': 'Hours_Remote',
    'If applicable: How many work-related tasks do you complete on an average day Onsite? This can be coding tasks, meetings, design etc. ': 'Tasks_Onsite',
    'If applicable: How many work-related tasks do you complete on an average day Remotely? This can be coding tasks, meetings, design etc. ': 'Tasks_Remote',
    'On a scale of 1 (much less) to 5 (much more), rate the level of support you receive from your company while working remotely.': 'Support_Level',
    'How frequently do you experience technical issues that impact your productivity when working remotely?': 'Tech_Issues',
    'On a scale from 1 (much less productive) to 5 (much more productive), how do you rate your productivity working remotely compared to onsite? ': 'Remote_Productivity'
}, inplace=True)

# Convert technical issues scale to numeric for correlation analysis (assuming "Very Frequently" = 5, "Never" = 1)
tech_issues_numeric = {
    "Always": 5,
    "Usually": 4,
    "Sometimes": 3,
    "Rarely": 2,
    "Never": 1
}

data_correlation['Tech_Issues'] = data_correlation['Tech_Issues'].map(tech_issues_numeric)

# Calculate correlation matrix
correlation_matrix = data_correlation.corr()

# Visualise the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix for Perceived Productivity and Related Variables')
plt.show()