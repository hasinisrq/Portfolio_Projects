import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Carlito', 'Calibri', 'DejaVu Sans']

periods = [
    '1996–2000', '2000–2003', '2003–2006', '2006–2010', '2010–2013',
    '2013–2016', '2016–2017', '2017–2022', '2022–2023', '2023–2024'
]
midpoints = [1998, 2001.5, 2004.5, 2008, 2011.5, 2014.5, 2016.5, 2019.5, 2022.5, 2023.5]

agriculture = [0.51, 1.25, -0.03, 0.41, 0.22, -0.28, -0.87, 1.74, -0.42, -0.63]
industry    = [0.37, 0.77, 0.45, 0.86, 0.69, 0.03, 0.24, -0.08, 0.28, -0.58]
services    = [0.20, 0.48, 0.81, 0.30, 0.22, 0.54, 1.26, 0.36, 0.48, -0.71]
overall     = [0.54, 0.89, 0.34, 0.50, 0.36, 0.11, 0.33, 0.42, 0.12, -0.63]

datasets = [
    ('Agriculture', agriculture, '#2E7D32'),
    ('Industry', industry, '#C62828'),
    ('Services', services, '#1565C0'),
    ('Overall Economy', overall, '#e65c00'),
]

fig, axes = plt.subplots(2, 2, figsize=(20, 18))
axes = axes.flatten()

for idx, (title, data, color) in enumerate(datasets):
    ax = axes[idx]

    ax.plot(
        midpoints, data,
        color=color, linewidth=3.2,
        marker='o', markersize=10,
        markerfacecolor=color,
        markeredgecolor='white',
        markeredgewidth=2,
        zorder=5
    )

    ax.axhline(y=0, color='#C00000', linewidth=1.3, linestyle='--', alpha=0.7, zorder=3)

    y_min = min(min(data) - 0.35, -0.9)
    y_max = max(max(data) + 0.35, 1.1)

    ax.axhspan(y_min, 0, color='#FFE0E0', alpha=0.4, zorder=1)

    for x, y in zip(midpoints, data):
        offset = 16 if y >= 0 else -20
        label_color = '#C00000' if y < 0 else color
        ax.annotate(
            f'{y:.2f}',
            xy=(x, y),
            fontsize=16,
            fontweight='bold',
            color=label_color,
            ha='center',
            va='bottom' if y >= 0 else 'top',
            xytext=(0, offset),
            textcoords='offset points'
        )

    ax.text(2024.45, max(0.55, y_max * 0.6), 'Responsive\ngrowth',
            fontsize=13, color='#666666', va='center', style='italic')
    ax.text(2024.45, 0.25, 'Moderate',
            fontsize=13, color='#666666', va='center', style='italic')
    ax.text(2024.45, 0.05, 'Jobless\ngrowth',
            fontsize=13, color='#999999', va='center', style='italic')
    ax.text(2024.45, y_min * 0.5, 'Negative\n(job losses)',
            fontsize=13, color='#C00000', va='center', style='italic')

    ax.set_xticks(midpoints)
    ax.set_xticklabels(periods, fontsize=14, rotation=40, ha='right')
    ax.set_ylabel('Employment Elasticity', fontsize=16, labelpad=12)
    ax.set_ylim(y_min, y_max)
    ax.set_xlim(min(midpoints) - 0.5, 2025.2)

    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.2))
    ax.tick_params(axis='y', labelsize=14)

    ax.set_title(f'Employment Elasticity: {title}', fontsize=24, fontweight='bold', pad=18)

    ax.grid(axis='y', color='#E0E0E0', linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')

    ax.tick_params(colors='#333333')

plt.tight_layout()
plt.subplots_adjust(
    bottom=0.08,
    top=0.95,
    hspace=0.45,
    wspace=0.30,
    right=0.90
)

plt.savefig('sectoral_elasticity_4panel.png', dpi=400, bbox_inches='tight')
plt.show()