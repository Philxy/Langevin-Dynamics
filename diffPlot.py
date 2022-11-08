import csv
import matplotlib.pyplot as plt
import numpy as np


MSDFile = open('MSD.csv', 'r')
csvreader = csv.reader(MSDFile)

plt.figure(figsize=(10/2.54, 8/2.54), dpi=80)

time = []
MSD = []
for row in csvreader:
    time.append(float(row[0]))
    MSD.append(float(row[1]))


plt.plot(time, MSD, label='Simulation')
plt.xlabel('Zeit $t$')
plt.ylabel(r'MSD $\langle \Delta \mathbf{x}(t)^2 \rangle$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


kBT = 1.0
friction = 1.0
m = 1.0

#plt.plot(time, [2.0 * kBT * t*t / m for t in time], label='Theory')
plt.plot(time, [4.0 * kBT / friction * t for t in time], label=r'$\langle \Delta\mathbf{r}(t)^2\rangle = 4 k_B T t / \lambda$', linestyle=':')

plt.legend()
plt.tight_layout()
plt.savefig('MSD.pdf')
plt.show()