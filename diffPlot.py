import csv
import matplotlib.pyplot as plt
import numpy as np





MSDFile = open('MSD.csv', 'r')
csvreader = csv.reader(MSDFile)


time = []
MSD = []
for row in csvreader:
    time.append(float(row[0]))
    MSD.append(float(row[1]))


plt.plot(time, MSD, label='Simulation')
plt.xlabel('Zeit $t$')
plt.ylabel(r'MSD $\langle \Delta \mathbf{x}(t)^2 \rangle$')


kBT = 5
friction = 0.1
m = 1

#plt.plot(time, [2.0 * kBT * t*t / m for t in time], label='Theory')
plt.plot(time, [4.0 * kBT / friction * t for t in time], label='Theory')

plt.legend()
plt.show()