import pandas as pd
import matplotlib.pyplot as plt

# Create the data for the Very High Vulnerable Cities (2017 and 2023)
data = {
    'Job Types': ['Managers', 'Professionals', 'Technicians & Associates', 'Clinical Support Workers',
                  'Service & Sales Workers', 'Agricultural, Forestry & Fishery Workers',
                  'Craft Related Trades Workers', 'Plant & Machine Operators', 'Elementary Occupations'],
    '2017': [0.00865, 0.05475, 0.0189, 0.0234, 0.1524, 0.46545, 0.1151, 0.0673, 0.09395],
    '2023': [0.01525, 0.0313, 0.02115, 0.00505, 0.1318, 0.54175, 0.0926, 0.07845, 0.08265]
}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the area graph with improved contrast (light pink for 2017 and dark purple for 2023)
ax.fill_between(df['Job Types'], df['2017'], color='#298c8c', alpha=0.8, label='2017')  # Teal
ax.fill_between(df['Job Types'], df['2023'], color='#f1a226', alpha=0.6, label='2023')  # Gold

# Add titles and labels with Calibri font and size 10
ax.set_title('Average Job Distribution in Very High Vulnerable Cities (2017 vs 2023)', fontsize=10, family='Calibri')
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