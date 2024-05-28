import pandas as pd
import matplotlib.pyplot as plt

#This script is written to produce a histogram of the data collected for percieved productivity of software engineers

# Load the Excel file to examine the content
file_path = "../Effects of Remote Work on the Productivity of Software Engineers (Responses).xlsx"
data = pd.read_excel(file_path)
data.head()

perceived_productivity = data['On a scale from 1 (much less productive) to 5 (much more productive), how do you rate your productivity working remotely compared to onsite? ']

# Histogram for Perceived Productivity
plt.figure(figsize=(8, 5))
plt.hist(perceived_productivity, bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of Perceived Productivity (Remote vs Onsite)')
plt.xlabel('Perceived Productivity Score')
plt.ylabel('Frequency')
plt.xticks(range(1, 6))  # Since the scale is from 1 to 5
plt.grid(axis='y', alpha=0.75)
plt.show()