import pandas as pd
import matplotlib.pyplot as plt

#This script is written to visualise the relation of the hours worked and tasks completed by software engineers in onsite and remote settings.

# Load the Excel file to examine the content
file_path = "../Effects of Remote Work on the Productivity of Software Engineers (Responses).xlsx"
data = pd.read_excel(file_path)
data.head()

hours_on_site = data["If applicable: On average, how many hours do you work per day Onsite ?"]
hours_remote = data["If applicable: On average, how many hours do you work per day Remotely?"]
tasks_on_site = data['If applicable: How many work-related tasks do you complete on an average day Onsite? This can be coding tasks, meetings, design etc. ']
tasks_remote = data['If applicable: How many work-related tasks do you complete on an average day Remotely? This can be coding tasks, meetings, design etc. ']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Box plot for hours worked
axes[0].boxplot([hours_on_site, hours_remote], labels=['Onsite', 'Remote'])
axes[0].set_title('Hours Worked Comparison')
axes[0].set_ylabel('Hours per Day')

# Box plot for tasks completed
axes[1].boxplot([tasks_on_site, tasks_remote], labels=['Onsite', 'Remote'])
axes[1].set_title('Tasks Completed Comparison')
axes[1].set_ylabel('Tasks per Day')

plt.tight_layout()
plt.show()