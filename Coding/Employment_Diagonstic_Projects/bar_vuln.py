import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Vulnerable Regions data for 2017 and 2023
data = {
    'Job Types': ['Managers', 'Professionals', 'Technicians & Associates', 'Clinical Support Workers',
                  'Service & Sales Workers', 'Agricultural, Forestry & Fishery Workers',
                  'Craft Related Trades Workers', 'Plant & Machine Operators', 'Elementary Occupations'],
    '2017': [0.010045, 0.048925, 0.015455, 0.014745, 0.14135, 0.39944, 0.12931, 0.05837, 0.18235],
    '2023': [0.01084, 0.044855, 0.0256, 0.006455, 0.122265, 0.496035, 0.10613, 0.07925, 0.108555]
}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Set the bar width
bar_width = 0.35

# Set up the x locations for the groups
index = np.arange(len(df['Job Types']))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars for 2017 and 2023, side-by-side
bar1 = ax.bar(index, df['2017'], bar_width, label='2017', color='#298c8c')  # Teal color for 2017
bar2 = ax.bar(index + bar_width, df['2023'], bar_width, label='2023', color='#f1a226')  # Gold color for 2023

# Add titles and labels with Calibri font and size 10
ax.set_title('Job Distribution in Vulnerable Regions (2017 vs 2023)', fontsize=10, family='Calibri')
ax.set_xlabel('Job Types', fontsize=10, family='Calibri')
ax.set_ylabel('Proportion', fontsize=10, family='Calibri')

# Set the x-axis labels
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(df['Job Types'], rotation=45, ha='right', fontsize=10, family='Calibri')

# Add the legend with Calibri font separately
ax.legend(fontsize=10, title_fontsize=10, loc='upper left', prop={'family': 'Calibri'})

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()