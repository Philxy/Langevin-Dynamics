import csv
import matplotlib.pyplot as plt
import numpy as np
import os

MSDFile = open('MSD.csv', 'r')
csvreader = csv.reader(MSDFile)

plt.figure(figsize=(16/2.54, 6/2.54), dpi=80)

f, ax1 = plt.subplots(figsize=(10/2.54, 8/2.54))



directory = 'trajectories/'


xPositions = []
yPositions = []


for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []
    
    for row in csvreader:
        t = float(row[0])
        if t < 10:
            continue
        time.append(t)
        xPositions.append(float(row[1]))
        yPositions.append(float(row[2]))

size = 2

H, xedges, yedges = np.histogram2d(xPositions, yPositions, bins=75, range=[[-size,size],[-size,size]])


H /= np.max(H)

cf = ax1.pcolormesh(yedges, xedges, H, cmap='viridis')
ax1.set_facecolor((68/256.0, 1/256.0, 84/256.0))


ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
cbar = f.colorbar(cf, ax=ax1, label=r'$N/N_{max}$')


ax1.set_yticks([-2,-1,0,1,2])
ax1.set_xticks([-2,-1,0,1,2])

plt.tight_layout()
plt.savefig('Figures/potential_period1.pdf')
#plt.show()


'''
time = []
MSD = []
for row in csvreader:
    time.append(float(row[0]))
    MSD.append(float(row[1]))


ax1.plot(time, MSD)
ax1.set_xlabel(r'Zeit $t$')
ax1.set_ylabel(r'MSD $\langle \Delta \mathbf{x}^2(t) \rangle$')

ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

kBT = 1.0
friction = 1.0
m = 1.0

'''
