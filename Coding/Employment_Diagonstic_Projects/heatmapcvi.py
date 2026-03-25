import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Load the district-level shapefile (Admin Level 2 - District boundaries)
district_shapefile = gpd.read_file(r"E:\RAPID\ADB - Employment Generation\Literature\Climate and Emp\Map\BGD_adm\BGD_adm2.shp")

# Step 2: Load the CVI data (CSV file)
cvi_data = pd.read_csv(r"E:\RAPID\ADB - Employment Generation\Literature\Climate and Emp\Map\district, cvi2.csv")

# Step 3: Check the column names in the shapefile to ensure proper merging
print(district_shapefile.columns)  # This helps identify the column name for district in the shapefile

# Step 4: Merge the shapefile with CVI data based on district name (adjust column names if needed)
# Assuming the column 'NAME_2' is the district name column in the shapefile and 'District' in the CSV
district_shapefile = district_shapefile.merge(cvi_data, left_on='NAME_2', right_on='District')

# Step 5: Plotting the map
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Create the heatmap based on the CVI values
district_shapefile.plot(
    column='CVI',            # Column with CVI values
    cmap='YlOrRd',           # Yellow → Orange → Red color scale
    linewidth=0.5,           # Border width for districts
    edgecolor='black',       # Border color
    legend=True,             # Show the legend
    legend_kwds={'label': "Climate Vulnerability Index (CVI)"},  # Legend label
    ax=ax
)

# Title and styling
ax.set_title("Bangladesh District-Level Climate Vulnerability Index (CVI)", fontsize=10)
ax.axis('off')  # Hide axis

# Step 6: Show the plot
plt.show()