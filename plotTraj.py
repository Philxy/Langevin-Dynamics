import csv
import matplotlib.pyplot as plt
import numpy as np
import os

import matplotlib.collections as mcoll
import matplotlib.path as mpath

directory = 'trajectories/'


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16.0/2.54, 8/2.54))


for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []
    xPositions = []
    yPositions = []
    for row in csvreader:
        time.append(float(row[0]))
        xPositions.append(float(row[1]))
        yPositions.append(float(row[2]))


    ax1.plot(time, xPositions)
    ax2.plot(xPositions,yPositions)


ax1.set_xlabel('Zeit $t$')
ax1.set_ylabel(r'$ x(t)-x(0)$')
ax2.set_ylabel('y')
ax2.set_xlabel('x')
#ax1.set_ylim(-370,370)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


plt.tight_layout()
plt.savefig('Figures/periodic.pdf')
plt.show()






'''
directory = 'trajectories/'


plt.figure(figsize=(12/2.54, 8/2.54), dpi=80)


for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []
    xPositions = []
    yPositions = []
    for row in csvreader:
        time.append(float(row[0]))
        xPositions.append(float(row[1]))
        yPositions.append(float(row[2]))

    if i < 20:
        
        plt.plot(time, xPositions)
    

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.xlabel('Zeit $t$')
plt.ylabel(r'$x(t)-x(0)$')
plt.ylim(-370,370)

plt.tight_layout()
plt.savefig('Figures/exemplary_disp.pdf')
plt.show()


'''
