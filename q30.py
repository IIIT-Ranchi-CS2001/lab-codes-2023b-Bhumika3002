'''Show party wise seat share for following results of the Assembly Elections 2023 in
Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached ( show the percentage seat share on each wedge )
Two pie charts as subplots on the same figure object
As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
Madhya Pradesh
BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)
Rajasthan
INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)'''



import matplotlib.pyplot as plt
import numpy as np

mp_data = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
rajasthan_data = {"INC": 69, "BJP": 115, "BSP": 2, "Others": 13}

mp_total = sum(mp_data.values())
mp_percentages = {party: (seats / mp_total) * 100 for party, seats in mp_data.items()}

rajasthan_total = sum(rajasthan_data.values())
rajasthan_percentages = {party: (seats / rajasthan_total) * 100 for party, seats in rajasthan_data.items()}

def create_pie_chart(ax, data, title):
    labels = list(data.keys())
    sizes = list(data.values())
    explode = [0.1 if size == max(sizes) else 0 for size in sizes]
    wedges, texts, autotexts = ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=90,
    )
    ax.set_title(title)

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
create_pie_chart(axs[0], mp_data, "Madhya Pradesh Seat Share")
create_pie_chart(axs[1], rajasthan_data, "Rajasthan Seat Share")

x = np.arange(len(mp_data))  
width = 0.35  

fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
bars1 = ax_bar.bar(x - width / 2, mp_data.values(), width, label="Madhya Pradesh")
bars2 = ax_bar.bar(x + width / 2, rajasthan_data.values(), width, label="Rajasthan")

ax_bar.set_xlabel("Party")
ax_bar.set_ylabel("Seats Won")
ax_bar.set_title("Seats Won by Party in Madhya Pradesh and Rajasthan")
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(mp_data.keys())
ax_bar.legend()

plt.tight_layout()
plt.show()
