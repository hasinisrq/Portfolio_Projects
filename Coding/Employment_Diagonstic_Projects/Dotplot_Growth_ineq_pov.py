import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

FONT = 'Calibri'

data = {
    'Bangladesh': {'GDP Growth\nRate, 2024': 4.223, 'Poverty Headcount\nRatio, 2020s': 5.9,   'Gini Index\nScore, 2020s': 30.9,   'Unemployment\nRate, 2024': 3.635},
    'Cambodia':   {'GDP Growth\nRate, 2024': 5.975, 'Poverty Headcount\nRatio, 2020s': None,  'Gini Index\nScore, 2020s': None,    'Unemployment\nRate, 2024': 0.254},
    'China':      {'GDP Growth\nRate, 2024': 4.977, 'Poverty Headcount\nRatio, 2020s': 0.0,   'Gini Index\nScore, 2020s': 36.267, 'Unemployment\nRate, 2024': 4.59},
    'India':      {'GDP Growth\nRate, 2024': 6.495, 'Poverty Headcount\nRatio, 2020s': 5.3,   'Gini Index\nScore, 2020s': 25.5,   'Unemployment\nRate, 2024': 4.173},
    'Indonesia':  {'GDP Growth\nRate, 2024': 5.030, 'Poverty Headcount\nRatio, 2020s': 7.68,  'Gini Index\nScore, 2020s': 35.46,  'Unemployment\nRate, 2024': 3.301},
    'Thailand':   {'GDP Growth\nRate, 2024': 2.542, 'Poverty Headcount\nRatio, 2020s': 0.025, 'Gini Index\nScore, 2020s': 34.425, 'Unemployment\nRate, 2024': 0.781},
    'Viet Nam':   {'GDP Growth\nRate, 2024': 7.091, 'Poverty Headcount\nRatio, 2020s': 1.45,  'Gini Index\nScore, 2020s': 36.45,  'Unemployment\nRate, 2024': 1.602},
}

colors = {
    'Bangladesh': '#C0392B',
    'Cambodia':   '#E07B54',
    'China':      '#27AE60',
    'India':      '#8E44AD',
    'Indonesia':  '#2980B9',
    'Thailand':   '#16A085',
    'Viet Nam':   '#C9A227',
}

markers = {
    'Bangladesh': 'o',
    'Cambodia':   's',
    'China':      'D',
    'India':      'X',
    'Indonesia':  '^',
    'Thailand':   'P',
    'Viet Nam':   '*',
}

indexes = list(list(data.values())[0].keys())
n_idx = len(indexes)
x_pos = np.arange(n_idx)

def norm(val, idx):
    vals = [v[idx] for v in data.values() if v[idx] is not None]
    lo, hi = min(vals), max(vals)
    if hi == lo: return 0.5
    return (val - lo) / (hi - lo)

all_points = {}
for country, vals in data.items():
    for xi, idx in enumerate(indexes):
        v = vals[idx]
        if v is not None:
            all_points[(xi, country)] = norm(v, idx)

MIN_GAP = 0.07
col_assignments = {}
for xi in x_pos:
    col = [(c, all_points[(xi, c)]) for c in data.keys() if (xi, c) in all_points]
    col.sort(key=lambda t: t[1])
    sides = {}
    side = 1
    for c, y in col:
        sides[c] = 1 if c == 'Bangladesh' else side
        if c != 'Bangladesh': side *= -1
    nudges = {c: 0.0 for c, _ in col}
    for i in range(1, len(col)):
        c_prev, y_prev = col[i-1]
        c_curr, y_curr = col[i]
        if abs(y_curr - y_prev - nudges[c_prev]) < MIN_GAP:
            nudges[c_curr] += MIN_GAP - (y_curr - y_prev)
    for c, y in col:
        col_assignments[(xi, c)] = {'side': sides[c], 'nudge': nudges[c]}

fig, ax = plt.subplots(figsize=(9, 6.5))
plt.subplots_adjust(left=0.06, right=0.76, top=0.88, bottom=0.18)

for xi in x_pos:
    ax.axvline(xi, color='#CCCCCC', linewidth=0.9, linestyle='--', zorder=0)

for country, vals in data.items():
    is_bdesh = country == 'Bangladesh'
    ms = 13 if is_bdesh else 9
    zorder = 5 if is_bdesh else 3

    for xi, idx in enumerate(indexes):
        v = vals[idx]
        if v is None:
            continue
        y = all_points[(xi, country)]
        asgn = col_assignments[(xi, country)]
        side = asgn['side']
        y_display = y + asgn['nudge']

        ax.plot(xi, y, marker=markers[country], color=colors[country],
                markersize=ms, zorder=zorder,
                markeredgewidth=0.6, markeredgecolor='white' if is_bdesh else colors[country])

        x_off = 0.1 * side
        ha = 'left' if side == 1 else 'right'
        fw = 'bold' if is_bdesh else 'normal'
        fs = 11 if is_bdesh else 10
        label = f'{country}\n{v:.2f}' if is_bdesh else country
        ax.text(xi + x_off, y_display, label,
                fontsize=fs, fontfamily=FONT, color=colors[country],
                va='center', ha=ha, fontweight=fw, zorder=6)

ax.set_xticks(x_pos)
ax.set_xticklabels(indexes, fontsize=11, fontfamily=FONT, ha='center')
ax.set_yticks([])
ax.set_xlim(-0.5, n_idx - 0.5)
ax.set_ylim(-0.1, 1.2)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#BBBBBB')
ax.tick_params(axis='x', colors='#333333', length=0, pad=10)

ax.set_title('Comparison of Country-wise Growth, Poverty and Inequality Positioned by Relative Performance across Indices',
             fontsize=13, fontfamily=FONT, fontweight='bold', pad=12)

ax.text(-0.48, 1.16, 'Higher value', fontsize=9, fontfamily=FONT, color='#999999', va='top')
ax.text(-0.48, -0.08, 'Lower value', fontsize=9, fontfamily=FONT, color='#999999', va='bottom')

legend_handles = [
    mlines.Line2D([], [], color=colors[c], marker=markers[c], linestyle='None',
                  markersize=10 if c == 'Bangladesh' else 8,
                  label=c, markeredgewidth=0.4)
    for c in data.keys()
]
ax.legend(handles=legend_handles, fontsize=10, frameon=False,
          loc='upper left', bbox_to_anchor=(1.02, 1.0),
          prop={'family': FONT, 'size': 10})

plt.savefig(r'D:\Ayon Important\Python\pythonProject\dotplot_v2.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.show()
print("Done")