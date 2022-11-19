import csv
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.optimize import curve_fit

directory = 'EscapeTrajectories/'


x_max = 1.1
y_max = 1.1


energies = []
taus = []

fig, (ax1, ax2) = plt.subplots(ncols=2,nrows=1, figsize=(16/2.54, 8/2.54))


for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    kBT = float(filename.split("_")[-1].replace('.csv', ''))

    csvreader = csv.reader(open(path, 'r'))
    time = []
    xPositions = []
    yPositions = []
    for row in csvreader:
        time = float(row[0])
        x = float(row[1])

        if (x) > x_max:
            energies.append(kBT)
            taus.append(time)
            break



for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    kBT = float(filename.split("_")[-1].replace('.csv', ''))

    

    csvreader = csv.reader(open(path, 'r'))
    time = []
    xPositions = []
    yPositions = []
    for row in csvreader:
        time = float(row[0])
        y = float(row[2])

        if (y) > y_max:
            energies.append(kBT)
            taus.append(time)
            break


energy_bins = np.linspace(0.001, 10.1, 10000)
taus_bins = np.zeros(energy_bins.size)
taus_count = np.zeros(energy_bins.size)
digitized = np.digitize(energies, energy_bins)

for n, index in enumerate(digitized):
    taus_bins[index] += taus[n]
    taus_count[index] += 1


for i in range(taus_bins.size):
    taus_bins[i] /= taus_count[i]


#plt.yscale('log')

import math

not_nan_indices = [i for i, value in enumerate(taus_bins) if not math.isnan(value)]


xdata = [energy_bins[i] for i in not_nan_indices]
ydata = [taus_bins[i] for i in not_nan_indices]

ax1.scatter(xdata,ydata)
ax2.scatter(np.reciprocal(xdata),ydata)

def func(kBT):
    return  np.exp(np.reciprocal(kBT) * 1/6.0) * 10

#popt, pcov = curve_fit(func, xdata, ydata)

x = np.linspace(np.min(xdata), max(xdata), 10000)

ax1.plot(x, func(x), linestyle=':')
ax2.plot(np.reciprocal(x), func(x), linestyle=':')
ax1.set_yscale('log')
ax1.set_xscale('log')
ax2.set_yscale('log')

ax1.set_ylabel(r'$\tau$')
ax2.set_ylabel(r'$\tau$')
ax1.set_xlabel(r'$k_BT$')
ax2.set_xlabel(r'$1/k_BT$')

plt.tight_layout()
plt.show()
