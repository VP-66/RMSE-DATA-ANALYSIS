import pandas as pd
import matplotlib.pyplot as plt

#This script is written to determine the descriptive statistics of the data collected for percieved productivity of software engineers

# Load the Excel file to examine the content
file_path = "../Effects of Remote Work on the Productivity of Software Engineers (Responses).xlsx"
data = pd.read_excel(file_path)
data.head()

# Descriptive Statistics for Perceived Productivity
perceived_productivity = data['On a scale from 1 (much less productive) to 5 (much more productive), how do you rate your productivity working remotely compared to onsite? ']

# Descriptive statistics
descriptive_stats_productivity = perceived_productivity.describe()

print(descriptive_stats_productivity)