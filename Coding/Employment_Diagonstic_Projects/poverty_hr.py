import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

FONT = 'Calibri'

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
x = np.arange(len(decades))

data = {
    'Bangladesh': [46.53, 47.3,  36.85, 22.3,  5.9],
    'China':      [89.93, 70.05, 35.8,  6.81,  0],
    'India':      [51.35, 47.5,  40.5,  27.1,  5.3],
    'Indonesia':  [86.5,  74.74, 47.06, 22.25, 7.68],
    'Thailand':   [28.85, 11.15, 3.07,  0.23,  0.025],
    'Viet Nam':   [None,  47.8,  28.875, 3.4,  1.45],
}

colors = {
    'Bangladesh': '#C0392B',
    'China':      '#E07B54',
    'India':      '#5B8DB8',
    'Indonesia':  '#6AAB6A',
    'Thailand':   '#9B72B0',
    'Viet Nam':   '#C9A227',
}

fig, ax = plt.subplots(figsize=(6.4, 4.2))

# Plot lines
for country, values in data.items():
    xs = [x[i] for i, v in enumerate(values) if v is not None]
    ys = [v for v in values if v is not None]
    lw = 2.5 if country == 'Bangladesh' else 1.3
    ms = 5.5 if country == 'Bangladesh' else 3.5
    ax.plot(xs, ys, color=colors[country], linewidth=lw,
            marker='o', markersize=ms, zorder=5 if country == 'Bangladesh' else 2)

# Arrow annotations — manually placed to avoid overlap
# Format: country -> (arrow_start_on_line: x_idx, label_xy, arrow_connectionstyle)
annotations = {
    'China':      dict(pt_idx=0, pt_val=89.93,  lxy=(0.6, 93),   conn='arc3,rad=-0.2'),
    'Indonesia':  dict(pt_idx=0, pt_val=86.5,   lxy=(-0.3, 80),  conn='arc3,rad=0.2'),
    'India':      dict(pt_idx=1, pt_val=47.5,   lxy=(0.3, 57),   conn='arc3,rad=-0.15'),
    'Viet Nam':   dict(pt_idx=1, pt_val=47.8,   lxy=(0.9, 38),   conn='arc3,rad=0.2'),
    'Bangladesh': dict(pt_idx=2, pt_val=36.85,  lxy=(1.2, 28),   conn='arc3,rad=0.2'),
    'Thailand':   dict(pt_idx=0, pt_val=28.85,  lxy=(-0.3, 20),  conn='arc3,rad=0.15'),
}

for country, ann in annotations.items():
    xi = ann['pt_idx']
    yi = ann['pt_val']
    lx, ly = ann['lxy']
    fw = 'bold' if country == 'Bangladesh' else 'normal'
    fs = 9 if country == 'Bangladesh' else 8.5
    ax.annotate(
        country,
        xy=(xi, yi),
        xytext=(lx, ly),
        fontsize=fs, fontfamily=FONT, fontweight=fw,
        color=colors[country],
        ha='center', va='center',
        arrowprops=dict(
            arrowstyle='->', color=colors[country],
            lw=1.0,
            connectionstyle=ann['conn']
        )
    )

# Axes
ax.set_xticks(x)
ax.set_xticklabels(decades, fontsize=10, fontfamily=FONT)
ax.set_yticks(range(0, 101, 10))
ax.set_yticklabels([f'{v}%' for v in range(0, 101, 10)], fontsize=10, fontfamily=FONT)
ax.set_ylabel('Poverty Headcount Ratio (%)', fontsize=10, fontfamily=FONT, labelpad=8)
ax.set_xlabel('Decade', fontsize=10, fontfamily=FONT, labelpad=8)
ax.set_title('Comparison of Country-wise Poverty Headcount Ratio at $3.00 a Day (2021 PPP), 1980s–2020s',
             fontsize=10, fontfamily=FONT, fontweight='bold', pad=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#BBBBBB')
ax.spines['bottom'].set_color('#BBBBBB')
ax.tick_params(axis='both', colors='#444444', length=3)
ax.yaxis.grid(True, color='#EEEEEE', linewidth=0.75, zorder=0)
ax.set_axisbelow(True)
ax.set_xlim(-0.6, 4.4)
ax.set_ylim(-2, 105)

plt.tight_layout()
plt.savefig(r'D:\Ayon Important\Python\pythonProject\poverty_headcount_v2.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.show()
print("Done")