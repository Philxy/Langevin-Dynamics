import csv
import matplotlib.pyplot as plt
import numpy as np


MSDFile = open('MSD.csv', 'r')
csvreader = csv.reader(MSDFile)

plt.figure(figsize=(16/2.54, 6/2.54), dpi=80)

f, ax1 = plt.subplots(figsize=(10/2.54, 8/2.54))

time = []
MSD = []
for row in csvreader:
    time.append(float(row[0]))
    MSD.append(float(row[1]))






plt.plot(time, MSD, label='Simulation')
plt.xlabel('Zeit $t$')
plt.ylabel(r'MSD $\langle \Delta \mathbf{x}(t)^2 \rangle$')



kBT = 1.0
friction = 1.0
m = 1.0

#ax1.plot(time, [2.0 * kBT * t*t / m for t in time], label='$k_BT t^2/m$')
ax1.plot(time, [2.0 * kBT / friction * t for t in time], label=r'$2 k_B T t / \lambda$', linestyle=':')

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

axins = ax1.inset_axes([0.2, 0.65, 0.3, 0.3])
axins.plot(time[:100], [2.0 * kBT * t*t / m for t in time][:100], label='$k_BT t^2/m$', color='tab:green', linestyle=':')

axins.plot(time[:100], MSD[:100], label='Simulation')
ax1.indicate_inset_zoom(axins, edgecolor="black")
plt.plot([],[],label='$k_BT t^2/m$', color='tab:green', linestyle=':')

plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('MSD.pdf')
plt.show()