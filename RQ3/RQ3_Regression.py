import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

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

# Prepare data for analysis by extracting the relevant columns
job_satisfaction = data['On a scale from 1 (very dissatisfied) to 5 (very satisfied), how satisfied are you with your current remote work arrangement? ']
company_support = data['On a scale of 1 (much less) to 5 (much more), rate the level of support you receive from your company while working remotely.']

# Descriptive statistics for job satisfaction and company support
descriptive_stats_job_satisfaction = job_satisfaction.describe()
descriptive_stats_company_support = company_support.describe()

# Include technical issues already mapped to numeric values for correlation and regression analysis
data_analysis = data_correlation[['Tech_Issues', 'Remote_Productivity']].copy()
data_analysis['Job Satisfaction'] = job_satisfaction.copy()
data_analysis['Company Support'] = company_support.copy()

# Prepare the data for regression analysis
X = data_analysis[['Tech_Issues']]
y = data_analysis['Remote_Productivity']

# Adding a constant to the independent variable for the intercept
X = sm.add_constant(X)

# Create a regression model
model = sm.OLS(y, X).fit()
model_summary = model.summary()

print(model.summary())

# Plotting the regression
plt.scatter(data_analysis[['Tech_Issues']], y, alpha=0.5)
plt.plot(data_analysis[['Tech_Issues']], model.predict(X), color='red')
plt.xlabel('Technical Issues (Numeric)')
plt.ylabel('Productivity Rating')
plt.title('Impact of Technical Issues on Productivity')
plt.show()