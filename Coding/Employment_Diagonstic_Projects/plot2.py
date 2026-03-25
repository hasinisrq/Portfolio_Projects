import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# ---- Force Calibri Font ----
mpl.rcParams['font.family'] = 'Calibri'

# Read Excel file
df = pd.read_excel("natural_disasters.xlsx", sheet_name="Sheet6")
df.columns = df.columns.str.strip()

years = pd.to_numeric(df["Year"], errors="coerce")
frequency = pd.to_numeric(df["Frequency of Natural Disasters"], errors="coerce")

mask = years.notna() & frequency.notna()
years = years[mask]
frequency = frequency[mask]

# Linear trend line
z = np.polyfit(years, frequency, 1)
p = np.poly1d(z)

# Create figure
plt.figure(figsize=(14, 6))

# Professional bars
plt.bar(
    years,
    frequency,
    color="#4C72B0",
    edgecolor="black",
    linewidth=0.5,
    alpha=0.85
)

# 🔴 Red dashed trend line
plt.plot(
    years,
    p(years),
    linestyle="--",
    color="red",
    linewidth=2
)

# 🔹 Vertical line after 1990
plt.axvline(x=1990 + 0.5, color="red", linestyle=":", linewidth=1.5)

# Axis labels
plt.xlabel("Year", fontsize=12)
plt.ylabel("Frequency of Natural Disasters", fontsize=12)

plt.xticks(years.iloc[::5], rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.3)

# Remove unnecessary borders
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.tight_layout()
plt.show()