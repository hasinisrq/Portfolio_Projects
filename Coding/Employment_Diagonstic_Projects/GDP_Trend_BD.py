import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# =========================
# 1. Load the data
# =========================
file_path = r"D:\Ayon Important\Python\pythonProject\.venv\GDP_trend_BD.csv"

df_raw = pd.read_csv(file_path)
df_raw.columns = df_raw.columns.str.strip()
df_raw = df_raw.dropna(axis=1, how='all')

# Rename first column
df_raw.rename(columns={df_raw.columns[0]: 'Series Name'}, inplace=True)
df_raw['Series Name'] = df_raw['Series Name'].astype(str).str.strip()

# =========================
# 2. Extract rows
# =========================
gdp_row = df_raw[df_raw['Series Name'] == 'GDP (current US$)']
growth_row = df_raw[df_raw['Series Name'] == 'GDP growth (annual %)']

year_cols = [col for col in df_raw.columns if str(col).strip().isdigit()]

df = pd.DataFrame({
    'Year': [int(y) for y in year_cols],
    'GDP': gdp_row[year_cols].iloc[0].values,
    'Growth': growth_row[year_cols].iloc[0].values
})

# =========================
# 3. Clean data
# =========================
df['GDP'] = pd.to_numeric(df['GDP'], errors='coerce')
df['Growth'] = pd.to_numeric(df['Growth'], errors='coerce')
df['GDP_Billion'] = df['GDP'] / 1e9

# =========================
# 4. Average growth calculations
# =========================
avg_1960_1980 = df[(df['Year'] >= 1960) & (df['Year'] <= 1980)]['Growth'].mean()
avg_1981_2000 = df[(df['Year'] >= 1981) & (df['Year'] <= 2000)]['Growth'].mean()
avg_2001_2024 = df[(df['Year'] >= 2001) & (df['Year'] <= 2024)]['Growth'].mean()

# =========================
# 5. Plot setup
# =========================
plt.rcParams['font.family'] = 'Calibri'

fig, ax1 = plt.subplots(figsize=(13.5, 7.5))
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')

# =========================
# 6. GDP bars
# =========================
bars = ax1.bar(
    df['Year'],
    df['GDP_Billion'],
    width=0.38,
    color='#4F81BD',
    edgecolor='#4F81BD',
    linewidth=0.6,
    zorder=2
)

# =========================
# 7. Primary axis formatting
# =========================
ax1.set_xlabel('Year', fontsize=11)
ax1.set_ylabel('GDP, in Billion USD', fontsize=11)

tick_positions = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
tick_labels = ['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4.0', '4.5', '5']

ax1.set_yticks(tick_positions)
ax1.set_yticklabels(tick_labels, fontsize=10)
ax1.set_ylim(0, 520)

ax1.set_xticks(df['Year'][::3])
ax1.set_xticklabels(df['Year'][::3], rotation=45, ha='right', fontsize=10)
ax1.tick_params(axis='both', length=0)

# =========================
# 8. Secondary axis for growth line
# =========================
ax2 = ax1.twinx()
line, = ax2.plot(
    df['Year'],
    df['Growth'],
    color='#C0504D',
    linewidth=3,
    zorder=3
)

ax2.set_ylabel('GDP Growth Rate', fontsize=11)
ax2.set_ylim(-20, 15)
ax2.tick_params(axis='y', labelsize=10, length=0)

# =========================
# 9. Divider lines
# =========================
ax1.axvline(x=1980.5, color='red', linestyle=':', linewidth=1.8, zorder=1)
ax1.axvline(x=2000.5, color='red', linestyle=':', linewidth=1.8, zorder=1)

# =========================
# 10. Remove all spines / box
# =========================
for spine in ax1.spines.values():
    spine.set_visible(False)

for spine in ax2.spines.values():
    spine.set_visible(False)

# =========================
# 11. Title
# =========================
plt.title('GDP Trend in Bangladesh, (1960-2024)', fontsize=15, pad=12)

# =========================
# 12. Legend
# =========================
legend_elements = [
    Patch(facecolor='#4F81BD', edgecolor='#4F81BD', label='GDP'),
    Line2D([0], [0], color='#C0504D', lw=3, label='GDP Growth Rate')
]

ax1.legend(
    handles=legend_elements,
    loc='lower center',
    bbox_to_anchor=(0.5, -0.17),
    ncol=2,
    frameon=False,
    fontsize=10
)

# =========================
# 13. Smaller annotation text
# =========================
ax2.text(
    1970, 13,
    f'Average GDP Growth Rate\n(1960-1980) = {avg_1960_1980:.2f}',
    ha='center', va='center', fontsize=12
)

ax2.text(
    1990.5, 13,
    f'Average GDP Growth Rate\n(1981-2000) = {avg_1981_2000:.2f}',
    ha='center', va='center', fontsize=12
)

ax2.text(
    2012, 13,
    f'Average GDP Growth Rate\n(2001-2024) = {avg_2001_2024:.2f}',
    ha='center', va='center', fontsize=12
)

# =========================
# 14. Tight layout
# =========================
plt.tight_layout()
plt.show()