import matplotlib.pyplot as plt
import numpy as np

FONT = 'Calibri'

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
x = np.arange(len(decades))

data = {
    'Bangladesh': [27.2,  30.25, 33.3,  32.25, 30.9],
    'China':      [28.23, 35.0,  41.97, 40.01, 36.27],
    'India':      [27.35, 26.1,  27.75, 28.8,  25.5],
    'Indonesia':  [31.35, 31.76, 31.2,  37.05, 35.46],
    'Thailand':   [44.5,  44.03, 41.24, 37.14, 34.43],
    'Viet Nam':   [None,  35.55, 36.3,  36.14, 36.45],
}

colors = {
    'Bangladesh': '#C0392B',
    'China':      '#E07B54',
    'India':      '#5B8DB8',
    'Indonesia':  '#6AAB6A',
    'Thailand':   '#9B72B0',
    'Viet Nam':   '#C9A227',
}

fig, ax = plt.subplots(figsize=(6.4, 4.4))
plt.subplots_adjust(left=0.18)

# Plot lines
for country, values in data.items():
    xs = [x[i] for i, v in enumerate(values) if v is not None]
    ys = [v for v in values if v is not None]
    lw = 2.5 if country == 'Bangladesh' else 1.3
    ms = 5.5 if country == 'Bangladesh' else 3.5
    ax.plot(xs, ys, color=colors[country], linewidth=lw,
            marker='o', markersize=ms, zorder=5 if country == 'Bangladesh' else 2)

# Arrow annotations — adjusted for new y range
annotations = {
    'Bangladesh': dict(pt_idx=2, pt_val=33.3,  lxy=(1.5, 28),   conn='arc3,rad=0.2'),
    'China':      dict(pt_idx=2, pt_val=41.97, lxy=(1.3, 46),   conn='arc3,rad=-0.15'),
    'India':      dict(pt_idx=0, pt_val=27.35, lxy=(-0.3, 27),  conn='arc3,rad=0.15'),
    'Indonesia':  dict(pt_idx=3, pt_val=37.05, lxy=(2.5, 40),   conn='arc3,rad=-0.2'),
    'Thailand':   dict(pt_idx=4, pt_val=34.43, lxy=(3.5, 48),   conn='arc3,rad=-0.2'),
    'Viet Nam':   dict(pt_idx=4, pt_val=36.45, lxy=(3.6, 32),   conn='arc3,rad=0.2'),
}

for country, ann in annotations.items():
    xi, yi = ann['pt_idx'], ann['pt_val']
    lx, ly = ann['lxy']
    fw = 'bold' if country == 'Bangladesh' else 'normal'
    fs = 9 if country == 'Bangladesh' else 8.5
    ax.annotate(
        country,
        xy=(xi, yi), xytext=(lx, ly),
        fontsize=fs, fontfamily=FONT, fontweight=fw,
        color=colors[country], ha='center', va='center',
        arrowprops=dict(arrowstyle='->', color=colors[country],
                        lw=1.0, connectionstyle=ann['conn'])
    )

# Axes styling
ax.set_xticks(x)
ax.set_xticklabels(decades, fontsize=10, fontfamily=FONT)
ax.set_yticks(range(25, 51, 5))
ax.set_yticklabels([str(v) for v in range(25, 51, 5)], fontsize=10, fontfamily=FONT)
ax.set_ylabel('Gini Index Score', fontsize=10, fontfamily=FONT, labelpad=28)
ax.set_xlabel('Decade', fontsize=10, fontfamily=FONT, labelpad=8)
ax.set_title('Comparison of Country-wise Gini Index Scores, 1980s–2020s',
             fontsize=10, fontfamily=FONT, fontweight='bold', pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#BBBBBB')
ax.spines['bottom'].set_color('#BBBBBB')
ax.tick_params(axis='both', colors='#444444', length=3)
ax.yaxis.grid(True, color='#EEEEEE', linewidth=0.75, zorder=0)
ax.set_axisbelow(True)
ax.set_xlim(-0.6, 4.6)
ax.set_ylim(24, 51)

# Compact inequality arrow
fig_x = 0.055
y_mid  = 0.50
half   = 0.10

fig.text(fig_x, y_mid + half + 0.035, 'Inequality', ha='center', va='bottom',
         fontsize=7, fontfamily=FONT, color='#666666')

ax.annotate('',
    xy=(fig_x, y_mid + half),     xycoords='figure fraction',
    xytext=(fig_x, y_mid - half), textcoords='figure fraction',
    arrowprops=dict(arrowstyle='->', color='#666666', lw=1.2)
)

plt.savefig(r'D:\Ayon Important\Python\pythonProject\poverty_headcount_v2.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.show()
print("Done")