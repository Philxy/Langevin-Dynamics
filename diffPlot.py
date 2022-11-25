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






ax1.plot(time, MSD, label='Simulation')
ax1.set_xlabel(r'$t/\tau_b$')
ax1.set_ylabel(r'MSD $\langle \Delta \mathbf{x}^2(t/\tau_b) \rangle$')
ax1.set_ylim(-0.0001, 0.0035)

ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

kBT = 1.0
friction = 1.0
m = 1.0

#ax1.plot(time, [2.0 * kBT * t*t / m for t in time], label='$k_BT t^2/m$')
#ax1.plot(time, [2.0 * kBT / friction * t for t in time], label=r'$2 k_B T t / \lambda$', linestyle=':')

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

t_max_index = 1000



axins = ax1.inset_axes([0.2, 0.5, 0.4, 0.4])
#axins.plot(time[:t_max_index], [ t*t * kBT/ m for t in time[:t_max_index]], label='$k_BT t^2/m$', color='tab:green', linestyle=':')

axins.plot(time[:t_max_index], MSD[:t_max_index], label='Simulation')
ax1.indicate_inset_zoom(axins, edgecolor="black")
plt.plot([],[],label='$k_BT t^2/m$', color='tab:green', linestyle=':')
#plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('MSD.pdf')
plt.show()