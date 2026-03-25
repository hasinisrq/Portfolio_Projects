import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the district-level shapefile (Admin Level 2 - District boundaries)
district_shapefile = gpd.read_file(r"E:\RAPID\ADB - Employment Generation\Literature\Climate and Emp\Map\BGD_adm\BGD_adm2.shp")

# Step 2: Load the Unemployment data (CSV file)
unemployment_data = pd.read_csv(r"E:\RAPID\ADB - Employment Generation\Data_Analysis\empcsv.csv")

# Step 3: Check the column names in the shapefile to ensure proper merging
print(district_shapefile.columns)  # This helps identify the column name for district in the shapefile
print(unemployment_data.columns)  # Check column names in CSV

# Step 4: Merge the shapefile with the Unemployment data based on district name (adjust column names if needed)
district_shapefile = district_shapefile.merge(unemployment_data, left_on='NAME_2', right_on='District')

# Step 5: Plotting the map
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Create the heatmap based on the unemployment rate values
district_shapefile.plot(
    column='Unemployment Mean',           # Column with Unemployment Mean values
    cmap='YlOrRd',                        # Yellow → Orange → Red color scale
    linewidth=0.5,                        # Border width for districts
    edgecolor='black',                    # Border color
    legend=True,                          # Show the legend
    legend_kwds={'label': "District Unemployment Rate (%)"},  # Legend label
    ax=ax
)

# Title and styling
ax.set_title("Bangladesh District-Level Unemployment Rate", fontsize=10, family='Calibri')  # Set font and size for the title
ax.axis('off')  # Hide axis

# Modify font for the legend
plt.legend(fontsize=10, prop={'family': 'Calibri'})  # Set Calibri font for legend

# Step 6: Show the plot
plt.show()