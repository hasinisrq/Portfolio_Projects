import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# -----------------------------
# DATA
# -----------------------------
data = [
("Bagerhat",0.52,45.76),("Bandarban",0.55,69.44),("Barguna",0.51,55.92),
("Barishal",0.53,33.32),("Bhola",0.53,46.13),("Bogura",0.49,51.22),
("Brahmanbaria",0.43,48.62),("Chandpur",0.47,35.99),("Chapainawabganj",0.48,44.17),
("Chattogram",0.46,24.35),("Chuadanga",0.46,55.86),("Cox's Bazar",0.52,58.38),
("Cumilla",0.46,27.87),("Dhaka",0.44,10.64),("Dinajpur",0.51,50.34),
("Faridpur",0.46,41.73),("Feni",0.44,47.65),("Gaibandha",0.53,54.42),
("Gazipur",0.44,16.56),("Gopalganj",0.47,36.66),("Habiganj",0.47,45.7),
("Jamalpur",0.51,50.41),("Jashore",0.47,40.73),("Jhalokati",0.48,28.05),
("Jhenaidah",0.46,58.95),("Joypurhat",0.45,55.79),("Khagrachhari",0.52,60.92),
("Khulna",0.52,30.78),("Kishoregonj",0.49,46.3),("Kurigram",0.51,53.52),
("Kushtia",0.46,50.36),("Lakshmipur",0.48,45.47),("Lalmonirhat",0.46,59),
("Madaripur",0.43,40.46),("Magura",0.47,45.58),("Manikganj",0.47,45.33),
("Meherpur",0.47,49.41),("Moulvibazar",0.44,63.91),("Munshiganj",0.41,27.06),
("Mymensingh",0.51,28.85),("Naogaon",0.50,53.04),("Narail",0.48,66.83),
("Narayanganj",0.42,7.26),("Narsingdi",0.44,23.53),("Natore",0.47,56.86),
("Netrakona",0.52,65.01),("Nilphamari",0.52,42.3),("Noakhali",0.49,59.67),
("Pabna",0.48,46.24),("Panchagarh",0.49,52.72),("Patuakhali",0.57,43.61),
("Pirojpur",0.50,31.76),("Rajbari",0.47,49.46),("Rajshahi",0.47,34.36),
("Rangamati",0.53,51.47),("Rangpur",0.51,37.89),("Satkhira",0.51,50.87),
("Shariatpur",0.46,56.46),("Sherpur",0.50,55.28),("Sirajganj",0.49,47.45),
("Sunamganj",0.51,55.44),("Sylhet",0.44,22.88),("Tangail",0.50,52.59),
("Thakurgaon",0.50,56.92)
]

df = pd.DataFrame(data, columns=["District","CVI","Agriculture"])

# -----------------------------
# COLOR RULES
# -----------------------------
very_high = {"Patuakhali","Bandarban"}

high = {
"Bagerhat","Barguna","Barishal","Bhola","Cox's Bazar","Dinajpur","Gaibandha",
"Jamalpur","Khagrachhari","Khulna","Kurigram","Mymensingh","Netrakona",
"Nilphamari","Rangamati","Rangpur","Satkhira","Sunamganj"
}

def color(d):
    if d in very_high:
        return "red"
    elif d in high:
        return "orange"
    else:
        return "green"

df["color"] = df["District"].apply(color)

# Bubble size
df["size"] = df["Agriculture"] * 15

# -----------------------------
# PLOT
# -----------------------------
plt.figure(figsize=(10,7))

plt.scatter(
    df["Agriculture"],
    df["CVI"],
    s=df["size"],
    c=df["color"],
    edgecolors="black",
    alpha=0.65
)

plt.xlabel("Agriculture Share (%)")
plt.ylabel("Climate Vulnerability Index (CVI)")
plt.title("Relationship Between Climate Vulnerability and Agricultural Employment Share Across Districts")

# Y axis range and ticks
plt.ylim(0.35,0.60)
plt.yticks([0.35,0.40,0.45,0.50,0.55,0.60])

plt.grid(alpha=0.3)

# Legend
legend_elements = [
Line2D([0],[0], marker='o', color='w', label='Very High Vulnerable',
       markerfacecolor='red', markeredgecolor='black', markersize=10),

Line2D([0],[0], marker='o', color='w', label='High Vulnerable',
       markerfacecolor='orange', markeredgecolor='black', markersize=10),

Line2D([0],[0], marker='o', color='w', label='Moderate to Low Vulnerable',
       markerfacecolor='green', markeredgecolor='black', markersize=10)
]

plt.legend(handles=legend_elements)

plt.tight_layout()
plt.show()