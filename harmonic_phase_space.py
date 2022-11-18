import csv
import matplotlib.pyplot as plt
import numpy as np
import os


directory = 'HarmonicTraj/'



fig, axs = plt.subplots(ncols=4, nrows=2, figsize=(26/2.52, 13/2.52))



for i, filename in enumerate(sorted(os.listdir(directory))):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []

    xPositions = []
    yPositions = []
    xVelocities = []
    yVelocities = []

    for row in csvreader:
        time.append(float(row[0]))
        xPositions.append(float(row[1]))
        xVelocities.append(float(row[3]))

    H, xedges, yedges = np.histogram2d(xPositions, xVelocities, bins=70)

    axs[0][i].plot(xPositions[:50000], xVelocities[:50000])
    axs[0][i].set_title('$k_B T=$' + filename.replace('.csv','').split('_')[1])
    axs[1][i].pcolormesh(yedges, xedges, H, cmap='viridis')
    axs[1][i].set_facecolor((68/256.0, 1/256.0, 84/256.0))

    axs[0][i].set_xlim(-1,1)
    axs[0][i].set_ylim(-1,1)
    axs[1][i].set_xlim(-1,1)
    axs[1][i].set_ylim(-1,1)
    axs[0][i].set_xlabel('$x$')
    axs[0][i].set_ylabel('$v$')
    axs[1][i].set_xlabel('$x$')
    axs[1][i].set_ylabel('$v$')

#plt.figure(figsize=(8/2.52, 6/2.52))

#plt.plot(xPositions, xVelocities)

axs[0][3].set_ylim(-3,3)
axs[1][3].set_xlim(-3,3)
axs[1][3].set_ylim(-3,3)
axs[0][3].set_xlim(-3,3)


plt.tight_layout()
plt.show()
