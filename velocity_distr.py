import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.integrate as integrate


directory = 'trajectories/'


f, axs = plt.subplots(ncols=1,nrows=2,figsize=(10/2.54, 12/2.54), dpi=80)


range = 3.4
box_width = 0.1

x = np.arange(-0, range, box_width)
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


velocities = []
norm_velocities = []

for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))

    for row in csvreader:
        time = float(row[0])
        vx = float(row[3])
        vy = float(row[4])
        vz = float(row[5])

        

        if time > 800:
            velocities.append(abs(vx))
            norm_velocities.append(np.sqrt(vy*vy + vx*vx + vz*vz ))


kT = 1.0
friction = 1.0
m = 1.0

D = 2 * kT / friction
t = 100

# Boltzmann
counts, bins = np.histogram(velocities, bins=np.arange(-0, range, box_width))
integral = integrate.simps(counts, bins[:-1])
axs[0].stairs(counts/integral, bins[:num_boxes], linewidth=1.5, label="Simulation")


def boltzmann(v):
    return (m / (2 * np.pi * kT))**(.5) * np.exp(-m * v*v / (2 * kT)) * 2.1

axs[0].plot(x, boltzmann(x), label='Boltzmann', alpha=0.8, color='tab:orange')

# Maxwell-Boltzmann
v = np.arange(0, 6, 0.1)
num_boxes = v.size
counts, bins = np.histogram(norm_velocities, bins=v)
integral = integrate.simps(counts, bins[:-1])
axs[1].stairs(counts/integral, bins[:num_boxes], linewidth=1.5, label="Simulation", color='tab:blue')


def maxwell_boltzmann(v):
    return (m / (2 * np.pi * kT))**(1.5) * 4*np.pi * v*v* np.exp(-m * v*v / (2 * kT)) 

axs[1].plot(v, maxwell_boltzmann(v), label='Maxwell-\nBoltzmann', alpha=0.8, color='tab:orange')
#axs[1].plot([],[],label='1D', color='tab:red')


axs[0].set_xlabel('$v_x$')
axs[0].set_ylabel('$p(v_x)$')
axs[1].set_xlabel(r'$|\mathbf{v}|$')
axs[1].set_ylabel(r'$p(|\mathbf{v}|)$')
axs[1].legend(loc='upper right')
axs[0].set_title('1D')
axs[1].set_title('3D')
plt.tight_layout()

plt.savefig('Figures/boltzmann_distr2.pdf')
plt.show()
