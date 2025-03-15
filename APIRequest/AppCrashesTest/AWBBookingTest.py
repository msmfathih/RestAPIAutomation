import matplotlib.pyplot as plt

# Data
labels = ['Quote & booking', 'Advance filter', 'Connectivity', 'Sorting & listing', 'Data privacy', 'Other UI issue']
sizes = [34, 4, 2, 1, 1, 7]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the pie chart
plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=150)

# Add a title
plt.title('Failed Test Case Distribution')

# Ensure a circular pie chart
plt.axis('equal')

# Show the plot
plt.show()