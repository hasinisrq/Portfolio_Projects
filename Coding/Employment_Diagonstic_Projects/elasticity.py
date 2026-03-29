import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

periods = [
    '2003–2006', '2006–2010', '2010–2013', '2013–2016',
    '2016–2017', '2017–2022', '2022–2023', '2023–2024'
]
elasticity = [0.39, 0.50, 0.36, 0.11, 0.33, 0.44, 0.12, -0.63]
midpoints = [2004.5, 2008, 2011.5, 2014.5, 2016.5, 2019.5, 2022.5, 2023.5]

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(midpoints, elasticity, color='#2E75B6', linewidth=2.5, marker='o',
        markersize=8, markerfacecolor='#2E75B6', markeredgecolor='white',
        markeredgewidth=1.5, zorder=5)

ax.axhline(y=0, color='#C00000', linewidth=1, linestyle='--', alpha=0.7, zorder=3)

for x, y in zip(midpoints, elasticity):
    offset = 12 if y >= 0 else -18
    color = '#C00000' if y < 0 else '#2E75B6'
    ax.annotate(f'{y:.2f}', xy=(x, y), fontsize=11, fontweight='bold',
                color=color, ha='center',
                va='bottom' if y >= 0 else 'top',
                xytext=(0, offset), textcoords='offset points')

ax.axhspan(-0.70, 0, color='#FFE0E0', alpha=0.4, zorder=1)

# Zone labels on right margin
ax.text(2024.2, 0.50, 'Responsive\ngrowth', fontsize=8, color='#666666', va='center', style='italic')
ax.text(2024.2, 0.25, 'Moderate', fontsize=8, color='#666666', va='center', style='italic')
ax.text(2024.2, 0.08, 'Jobless\ngrowth', fontsize=8, color='#999999', va='center', style='italic')
ax.text(2024.2, -0.35, 'Negative\n(job losses)', fontsize=8, color='#C00000', va='center', style='italic')

ax.set_xticks(midpoints)
ax.set_xticklabels(periods, fontsize=10, rotation=30, ha='right')
ax.set_ylabel('Employment Elasticity of GDP Growth', fontsize=9, labelpad=10)
ax.set_ylim(-0.80, 0.70)
ax.yaxis.set_major_locator(mticker.MultipleLocator(0.10))
ax.set_title('Employment Elasticity of GDP Growth in Bangladesh, 2003–2024',
             fontsize=10, fontweight='bold', pad=15)
ax.grid(axis='y', color='#E0E0E0', linewidth=0.8, zorder=0)
ax.set_axisbelow(True)


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')
ax.tick_params(colors='#333333', labelsize=10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.08, right=0.88)
plt.savefig('employment_elasticity_chart.png', dpi=300, bbox_inches='tight')
plt.show()