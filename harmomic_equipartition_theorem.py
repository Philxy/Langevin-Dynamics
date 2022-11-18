import csv
import matplotlib.pyplot as plt
import numpy as np


MSDFile = open('MSD.csv', 'r')
csvreader = csv.reader(MSDFile)

plt.figure(figsize=(8/2.54, 8/2.54), dpi=80)

time = []
MSD = []
for row in csvreader:
    time.append(float(row[0]))
    MSD.append(float(row[1]))


plt.xlabel('Zeit $t$')
plt.ylabel(r'$\langle \mathbf{v}(t)\mathbf{v}(0) \rangle$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))




kBT = 1.0
friction = 0.1
m = 1.0
v0 = np.sqrt(1)

#plt.axhline(y=1 * kBT/m, linestyle='dashed', label=r'$k_BT/m$', linewidth=2, color='black')


t = np.arange(0,100, 0.001)

#y = v0**2 * np.exp(-2*friction*t/m) +  2* kBT * friction / (2*friction*m) * (1-np.exp(-2*friction*t/m))

y = v0**2 * np.exp(-friction*t/m)



plt.plot(time, MSD, label='Simulation', alpha=0.8, color='tab:blue', linewidth=2)
plt.plot(t,y, label=r'Theorie', alpha=1, linestyle=':', color='tab:orange', linewidth=2)


plt.legend()
plt.tight_layout()
plt.savefig('Figures/sheesh.pdf')
plt.show()