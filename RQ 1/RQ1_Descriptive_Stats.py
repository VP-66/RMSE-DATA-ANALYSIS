import pandas as pd

#This script is written to determine the descriptive statistics of the hours worked and tasks completed by software engineers in onsite and remote settings.

# Load the Excel file to examine the content
file_path = "../Effects of Remote Work on the Productivity of Software Engineers (Responses).xlsx"
data = pd.read_excel(file_path)
data.head()

# To assess the impact of remote work on hours worked and tasks completed, we'll compare hours and tasks for onsite and remote settings.

# Descriptive Statistics for hours worked and tasks completed
hours_on_site = data["If applicable: On average, how many hours do you work per day Onsite ?"]
hours_remote = data["If applicable: On average, how many hours do you work per day Remotely?"]
tasks_on_site = data['If applicable: How many work-related tasks do you complete on an average day Onsite? This can be coding tasks, meetings, design etc. ']
tasks_remote = data['If applicable: How many work-related tasks do you complete on an average day Remotely? This can be coding tasks, meetings, design etc. ']

descriptive_stats_hours = pd.DataFrame({
    "Hours Onsite": hours_on_site.describe(),
    "Hours Remote": hours_remote.describe()
})

descriptive_stats_tasks = pd.DataFrame({
    "Tasks Onsite": tasks_on_site.describe(),
    "Tasks Remote": tasks_remote.describe()
})

print(descriptive_stats_hours)
print()
print(descriptive_stats_tasks)