import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.integrate as integrate

directory = 'trajectories/'


plt.figure(figsize=(12/2.54, 8/2.54), dpi=80)


range = 150
box_width = 3

x = np.arange(-range,+range,box_width)
n = [0] * x.size

num_boxes = x.size

def count(data):
    for pos in data:
        if abs(pos) > range:
            continue
        index = 0

        if pos > 0:
            index = int(abs(pos) / range * num_boxes + num_boxes/2)
        else: 
            index = int(abs(pos) / range * num_boxes)
        print(index)
        n[index] += 1
    

positions1 = []
positions2 = []
positions3 = []

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
    positions1.append(xPositions[0])
    positions1.append(yPositions[0])
    positions2.append(xPositions[1])
    positions2.append(yPositions[1])
    positions3.append(yPositions[2])
    positions3.append(yPositions[2])

    print(i)


kT = 1.0
friction = 1.0

D = 2 * kT / friction
t = 100


counts, bins = np.histogram(positions1, bins = np.arange(-range,range,box_width))
integral = integrate.simps(counts,bins[:-1],)
plt.stairs(counts/integral,bins[:num_boxes],linewidth=1.5, label=r'$t=0.1\cdot t_\mathrm{max}$')


counts, bins = np.histogram(positions2, bins = np.arange(-range,range,box_width))
integral = integrate.simps(counts,bins[:-1],)
plt.stairs(counts/integral,bins[:num_boxes],linewidth=1.5, label=r'$t=0.5\cdot t_\mathrm{max}$')


counts, bins = np.histogram(positions3, bins = np.arange(-range,range,box_width))
integral = integrate.simps(counts,bins[:-1],)
plt.stairs(counts/integral,bins[:num_boxes],linewidth=1.5, label=r'$t=1.0 \cdot t_\mathrm{max}$')

#plt.plot(bins, np.exp(-bins*bins/(2*t) * np.reciprocal(np.sqrt(2*np.pi*t))))


plt.xlabel('$x$')
plt.ylabel('Wahrscheinlichkeitsdichte $p(x)$')
plt.tight_layout()
plt.legend()
plt.savefig('Figures/position_prob_density_N_10000_dt_0.05.pdf')
plt.show()