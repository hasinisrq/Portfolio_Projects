import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the district-level shapefile (Admin Level 2 - District boundaries)
district_shapefile = gpd.read_file(r"E:\RAPID\ADB - Employment Generation\Literature\Climate and Emp\Map\BGD_adm\BGD_adm2.shp")

# Step 2: Load the Wage Mean data (CSV file)
wage_data = pd.read_csv(r"E:\RAPID\ADB - Employment Generation\Data_Analysis\wagexl.csv")

# Step 3: Check the column names in the shapefile to ensure proper merging
print(district_shapefile.columns)  # This helps identify the column name for district in the shapefile
print(wage_data.columns)          # Check column names in CSV

# Step 4: Merge the shapefile with the Wage data based on district name (adjust column names if needed)
district_shapefile = district_shapefile.merge(wage_data, left_on='NAME_2', right_on='District')

# Step 5: Plotting the map
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Create the heatmap based on the wage mean values
district_shapefile.plot(
    column='Wage Mean',           # Column with Wage Mean values
    cmap='RdYlGn',                # Red → Yellow → Green color scale (for lower to higher values)
    linewidth=0.5,                # Border width for districts
    edgecolor='black',            # Border color
    legend=True,                  # Show the legend
    legend_kwds={'label': "District Mean Wage (BDT)"},  # Legend label
    ax=ax
)

# Title and styling
ax.set_title("Bangladesh District-Level Mean Wage Comparison", fontsize=10, family='Calibri')  # Set font and size for the title
ax.axis('off')  # Hide axis

# Modify font for the legend (corrected version)
plt.legend(fontsize=10, prop={'family': 'Calibri'})  # Set Calibri font for legend

# Step 6: Show the plot
plt.show()