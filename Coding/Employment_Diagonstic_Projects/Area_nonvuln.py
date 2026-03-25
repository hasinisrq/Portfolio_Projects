import pandas as pd
import matplotlib.pyplot as plt

# Create the Non-Vulnerable Regions data for 2017 and 2023
data_non_vulnerable = {
    'Job Types': ['Managers', 'Professionals', 'Technicians & Associates', 'Clinical Support Workers',
                  'Service & Sales Workers', 'Agricultural, Forestry & Fishery Workers',
                  'Craft Related Trades Workers', 'Plant & Machine Operators', 'Elementary Occupations'],
    '2017': [0.012034091, 0.043756818, 0.017979545, 0.013618182, 0.159513636, 0.354981818, 0.155897727, 0.067765909, 0.174438636],
    '2023': [0.0138, 0.050295455, 0.030143182, 0.009502273, 0.14535, 0.444609091, 0.134204545, 0.075077273, 0.096988636]
}

# Convert the data to a pandas DataFrame
df_non_vulnerable = pd.DataFrame(data_non_vulnerable)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the area graph with teal for 2017 and gold for 2023
ax.fill_between(df_non_vulnerable['Job Types'], df_non_vulnerable['2017'], color='#298c8c', alpha=0.8, label='2017')  # Teal
ax.fill_between(df_non_vulnerable['Job Types'], df_non_vulnerable['2023'], color='#f1a226', alpha=0.6, label='2023')  # Gold

# Add titles and labels with Calibri font and size 10
ax.set_title('Average Job Distribution in Non-Vulnerable Regions (2017 vs 2023)', fontsize=10, family='Calibri')
ax.set_xlabel('Job Types', fontsize=10, family='Calibri')
ax.set_ylabel('Proportion', fontsize=10, family='Calibri')

# Set the font size for the tick labels
plt.xticks(rotation=45, ha='right', fontsize=10, family='Calibri')
plt.yticks(fontsize=10, family='Calibri')

# Set legend with Calibri font separately
ax.legend(fontsize=10, title_fontsize=10, loc='upper left', labels=['2017', '2023'], prop={'family': 'Calibri'})

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()