import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Aptos', 'Aptos Display', 'Carlito', 'Calibri', 'DejaVu Sans']

periods_data = {
    '2000-2010 (Growth-enhancing)': {
        'Agriculture': (-4.2, 0.38, 51.7),
        'Industry':    ( 4.2, 1.55, 13.5),
        'Services':    ( 0.5, 1.70, 34.8),
    },
    '2010-2017 (Growth-enhancing)': {
        'Agriculture': (-6.9, 0.36, 47.5),
        'Industry':    ( 2.7, 1.45, 17.7),
        'Services':    ( 3.7, 1.62, 35.3),
    },
    '2017-2024 (Growth-reducing)': {
        'Agriculture': ( 4.1, 0.34, 40.6),
        'Industry':    (-3.1, 1.62, 20.4),
        'Services':    (-1.0, 1.37, 39.0),
    },
    '2000-2024 (Full period)': {
        'Agriculture': (-7.0, 0.38, 51.7),
        'Industry':    ( 3.8, 1.55, 13.5),
        'Services':    ( 3.2, 1.70, 34.8),
    },
}

period_markers = {
    '2000-2010 (Growth-enhancing)': 'o',
    '2010-2017 (Growth-enhancing)': 's',
    '2017-2024 (Growth-reducing)':  '*',
    '2000-2024 (Full period)':      'D',
}

period_tags = {
    '2000-2010 (Growth-enhancing)': '00–10',
    '2010-2017 (Growth-enhancing)': '10–17',
    '2017-2024 (Growth-reducing)':  '17–24',
    '2000-2024 (Full period)':      '00–24',
}

colors = {'Agriculture': '#2E7D32', 'Industry': '#C62828', 'Services': '#0F4761'}

label_offsets = {
    # 2000-2010 (circles)
    ('2000-2010 (Growth-enhancing)', 'Agriculture'): ( 2.0, -0.15, 'left',   True),
    ('2000-2010 (Growth-enhancing)', 'Industry'):    ( 2.0,  0.18, 'left',   True),
    ('2000-2010 (Growth-enhancing)', 'Services'):    (-2.5,  0.25, 'right',  True),

    # 2010-2017 (squares)
    ('2010-2017 (Growth-enhancing)', 'Agriculture'): (-0.5,  0.30, 'right',  True),
    ('2010-2017 (Growth-enhancing)', 'Industry'):    (-3.0, -0.18, 'right',  True),
    ('2010-2017 (Growth-enhancing)', 'Services'):    ( 2.5, -0.05, 'left',   True),

    # 2017-2024 (stars)
    ('2017-2024 (Growth-reducing)',  'Agriculture'): ( 1.0,  0.25, 'left',   True),
    ('2017-2024 (Growth-reducing)',  'Industry'):    (-1.0,  0.30, 'right',  True),
    ('2017-2024 (Growth-reducing)',  'Services'):    ( 1.5, -0.30, 'left',   True),

    # 2000-2024 (diamonds)
    ('2000-2024 (Full period)',      'Agriculture'): (-2.5,  0.30, 'right',  True),
    ('2000-2024 (Full period)',      'Industry'):    ( 0.5,  0.45, 'left',   True),
    ('2000-2024 (Full period)',      'Services'):    (-2.5,  0.30, 'right',  True),
}

fig, ax = plt.subplots(figsize=(22, 14))

all_x = [v[0] for d in periods_data.values() for v in d.values()]
x_min, x_max = min(all_x) - 5, max(all_x) + 6
y_min, y_max = 0.0, 2.3
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

y_frac_at_1 = 1.0 / 2.3
ax.axvspan(0, x_max, ymin=y_frac_at_1, ymax=1.0, color='#C8E6C9', alpha=0.45, zorder=0)
ax.axvspan(x_min, 0, ymin=0, ymax=y_frac_at_1, color='#C8E6C9', alpha=0.45, zorder=0)
ax.axvspan(x_min, 0, ymin=y_frac_at_1, ymax=1.0, color='#FFCDD2', alpha=0.45, zorder=0)
ax.axvspan(0, x_max, ymin=0, ymax=y_frac_at_1, color='#FFCDD2', alpha=0.45, zorder=0)

ax.axhline(y=1.0, color='#666666', linewidth=1.8, linestyle='--', alpha=0.7, zorder=2)
ax.axvline(x=0,   color='#666666', linewidth=1.8, linestyle='--', alpha=0.7, zorder=2)

for period_label, sectors in periods_data.items():
    marker = period_markers[period_label]
    tag = period_tags[period_label]
    size_scale = 38 if marker == '*' else 26  # stars look smaller at the same s

    for sector, (x, y, share) in sectors.items():
        ax.scatter(x, y, s=share * size_scale, c=colors[sector], marker=marker,
                   alpha=0.85, edgecolors='white', linewidth=2.5, zorder=5)

        x_off, y_off, ha_val, use_arrow = label_offsets[(period_label, sector)]
        label_text = f'{sector[:3]} {tag}\n({x:+.1f}pp)'

        if use_arrow:
            ax.annotate(label_text, xy=(x, y),
                        xytext=(x + x_off, y + y_off),
                        fontsize=18, fontweight='bold', color=colors[sector],
                        ha=ha_val, va='center',
                        arrowprops=dict(arrowstyle='-', color=colors[sector],
                                        lw=1.2, alpha=0.6,
                                        connectionstyle='arc3,rad=0'))
        else:
            ax.annotate(label_text, xy=(x + x_off, y + y_off),
                        fontsize=18, fontweight='bold', color=colors[sector],
                        ha=ha_val, va='center')

ax.text(x_max - 0.3, 1.06, 'Above-average productivity', fontsize=18, color='#444444',
        ha='right', va='bottom', style='italic')
ax.text(x_max - 0.3, 0.94, 'Below-average productivity', fontsize=18, color='#444444',
        ha='right', va='top', style='italic')
ax.text(x_max - 0.3, 2.22, 'Gaining employment share →', fontsize=17, color='#444444',
        ha='right', va='top', style='italic')
ax.text(0.2, 2.22, '← Losing employment share', fontsize=17, color='#444444',
        ha='left', va='top', style='italic')

ax.set_xlabel('Change in Employment Share (percentage points)',
              fontsize=22, fontweight='bold', labelpad=14)
ax.set_ylabel('Relative Productivity (Sector / Total)',
              fontsize=22, fontweight='bold', labelpad=14)


ax.tick_params(labelsize=18)
ax.grid(True, alpha=0.25, zorder=0)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')

sector_legend = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['Agriculture'],
           markersize=18, label='Agriculture'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['Industry'],
           markersize=18, label='Industry'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['Services'],
           markersize=18, label='Services'),
]
period_legend = [
    Line2D([0], [0], marker=period_markers[p], color='w', markerfacecolor='#555555',
           markersize=18 if period_markers[p] != '*' else 22, label=p)
    for p in periods_data.keys()
]

leg1 = ax.legend(handles=sector_legend, loc='upper left', title='Sector',
                 fontsize=17, title_fontsize=18, frameon=True, framealpha=0.95,
                 edgecolor='#BBBBBB')
leg1._legend_box.align = 'left'
ax.add_artist(leg1)
leg2 = ax.legend(handles=period_legend, loc='lower left', title='Period (marker)',
                 fontsize=16, title_fontsize=18, frameon=True, framealpha=0.95,
                 edgecolor='#BBBBBB')
leg2._legend_box.align = 'left'

plt.tight_layout()
plt.savefig('2_MR_combined.png', dpi=300, bbox_inches='tight')
plt.show()