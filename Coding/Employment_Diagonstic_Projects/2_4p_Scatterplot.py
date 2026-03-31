import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Carlito', 'Calibri', 'DejaVu Sans']

periods_data = {
    '2000-2010 (Growth-enhancing)': {
        'Agriculture': (-3.26, 0.389, 50.8),
        'Industry':    (4.48, 1.603, 13.1),
        'Services':    (-0.85, 1.640, 36.2),
    },
    '2010-2016 (Growth-enhancing)': {
        'Agriculture': (-4.82, 0.357, 47.5),
        'Industry':    (2.91, 1.466, 17.6),
        'Services':    (1.59, 1.623, 35.3),
    },
    '2016-2024 (Growth-reducing)': {
        'Agriculture': (2.00, 0.329, 42.7),
        'Industry':    (-3.10, 1.585, 20.5),
        'Services':    (1.06, 1.450, 36.9),
    },
    '2000-2024 (Full period)': {
        'Agriculture': (-6.09, 0.389, 50.8),
        'Industry':    (4.29, 1.603, 13.1),
        'Services':    (1.80, 1.640, 36.2),
    },
}

colors = {'Agriculture': '#2E7D32', 'Industry': '#C62828', 'Services': '#1565C0'}

fig, axes = plt.subplots(2, 2, figsize=(28, 22))
axes = axes.flatten()

for idx, (period_label, sectors) in enumerate(periods_data.items()):
    ax = axes[idx]

    all_x = [v[0] for v in sectors.values()]
    x_margin = max(abs(min(all_x)), abs(max(all_x))) * 0.5 + 3
    x_min = min(all_x) - x_margin
    x_max = max(all_x) + x_margin
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.0, 2.2)

    ax.axhspan(1.0, 2.2, xmin=0.5, xmax=1.0, color='#C8E6C9', alpha=0.5, zorder=0)
    ax.axhspan(0.0, 1.0, xmin=0.0, xmax=0.5, color='#C8E6C9', alpha=0.5, zorder=0)
    ax.axhspan(1.0, 2.2, xmin=0.0, xmax=0.5, color='#FFCDD2', alpha=0.5, zorder=0)
    ax.axhspan(0.0, 1.0, xmin=0.5, xmax=1.0, color='#FFCDD2', alpha=0.5, zorder=0)

    for name, (x, y, size) in sectors.items():
        ax.scatter(x, y, s=size * 30, c=colors[name], alpha=0.8, edgecolors='white',
                   linewidth=2, zorder=5)
        if name == 'Agriculture':
            x_off, y_off, ha_val = 0, -0.15, 'center'
        elif name == 'Industry':
            x_off, y_off, ha_val = 0.4, 0.10, 'left'
        else:
            x_off, y_off, ha_val = 0.4, -0.10, 'left'

        ax.annotate(f'{name}\n({x:+.1f}pp)', xy=(x, y),
                    xytext=(x + x_off, y + y_off),
                    fontsize=22, fontweight='bold', color=colors[name],
                    ha=ha_val, va='center')

    ax.axhline(y=1.0, color='#666666', linewidth=1.5, linestyle='--', alpha=0.7, zorder=2)
    ax.axvline(x=0, color='#666666', linewidth=1.5, linestyle='--', alpha=0.7, zorder=2)

    ax.text(x_max - 0.3, 1.07, 'Above-average productivity', fontsize=16, color='#444444',
            ha='right', va='bottom', style='italic')
    ax.text(x_max - 0.3, 0.91, 'Below-average productivity', fontsize=16, color='#444444',
            ha='right', va='top', style='italic')

    ax.set_xlabel('Change in Employment Share (pp)', fontsize=20, fontweight='bold', labelpad=10)
    ax.set_ylabel('Relative Productivity\n(Sector / Total)', fontsize=20, fontweight='bold', labelpad=10)
    ax.set_title(period_label, fontsize=24, fontweight='bold', pad=18)

    ax.tick_params(labelsize=18)
    ax.grid(True, alpha=0.25, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')

legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#2E7D32', markersize=18, label='Agriculture'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#C62828', markersize=18, label='Industry'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#1565C0', markersize=18, label='Services'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=20,
           bbox_to_anchor=(0.5, 0.03), frameon=False)


plt.tight_layout()
plt.subplots_adjust(bottom=0.08, hspace=0.30, wspace=0.22)
plt.savefig('structural_transformation_scatter.png', dpi=300, bbox_inches='tight')
plt.show()