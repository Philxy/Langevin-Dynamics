import csv
import matplotlib.pyplot as plt
import numpy as np


f = open('correlogram.csv', 'r')
csvreader = csv.reader(f)


time = []
corr = []
for row in csvreader:
    time.append(float(row[0]))
    corr.append(float(row[1]))


plt.figure(figsize=(8/2.25,8/2.52))

plt.axhline(y=2, label=r'$2k_BT\lambda$', linestyle=':', color='tab:orange', linewidth=3)

plt.xlabel('$n$')
plt.ylabel(r'$\langle \zeta(t)\cdot \zeta(t+n \cdot \Delta t) \rangle$')

plt.plot(time,corr)
plt.legend()
plt.tight_layout()
plt.savefig('Figures/ACF.pdf')
plt.show()