import pandas as pd
import matplotlib.pyplot as plt

# Create the vulnerable region data for 2017 and 2023
data_vulnerable = {
    'Job Types': ['Managers', 'Professionals', 'Technicians & Associates', 'Clinical Support Workers',
                  'Service & Sales Workers', 'Agricultural, Forestry & Fishery Workers',
                  'Craft Related Trades Workers', 'Plant & Machine Operators', 'Elementary Occupations'],
    '2017': [0.010045, 0.048925, 0.015455, 0.014745, 0.14135, 0.39944, 0.12931, 0.05837, 0.18235],
    '2023': [0.01084, 0.044855, 0.0256, 0.006455, 0.122265, 0.496035, 0.10613, 0.07925, 0.108555]
}

# Convert the data to a pandas DataFrame
df_vulnerable = pd.DataFrame(data_vulnerable)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the area graph with teal for 2017 and gold for 2023
ax.fill_between(df_vulnerable['Job Types'], df_vulnerable['2017'], color='#298c8c', alpha=0.8, label='2017')  # Teal
ax.fill_between(df_vulnerable['Job Types'], df_vulnerable['2023'], color='#f1a226', alpha=0.6, label='2023')  # Gold

# Add titles and labels with Calibri font and size 10
ax.set_title('Average Job Distribution in Vulnerable Regions (2017 vs 2023)', fontsize=10, family='Calibri')
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