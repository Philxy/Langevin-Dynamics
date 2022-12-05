import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib

directory = 'ActiveTrajV00/'



f, ax = plt.subplots(ncols=2, nrows=1,figsize=(16/2.54, 8/2.54), dpi=80)

t_max = 1

labels = []

for i, filename in enumerate(sorted(os.listdir(directory))):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    times = []
    x = []
    y = []
    label = (filename.split('.')[0])

    for row in csvreader:

        t = float(row[0])
        if t > t_max:
            break

        times.append(t)
        x.append(float(row[1])*1.7)
        y.append(float(row[2])*1.7)

    ax[0].plot(x,y, label=label)

    ax[0].set_title('$v_0 = 0$')

    ax[0].set_xlim(-2.4,2.4)
    ax[0].set_ylim(-2.4,2.4)

    '''
    x_max = max(np.abs(x))
    y_max = max(np.abs(y))
    size = np.max([y_max, x_max])
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    '''

directory = 'ActiveTrajV04/'

for i, filename in enumerate(sorted(os.listdir(directory))):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    times = []
    x = []
    y = []
    label = (filename.split('.')[0])

    for row in csvreader:

        t = float(row[0])
        if t > t_max:
            break

        times.append(t)
        x.append(float(row[1]))
        y.append(float(row[2]))

    ax[1].set_title('$v_0 = 2$')

    ax[1].plot(x,y, label=label)
    ax[1].set_xlim(-2.4,2.4)
    ax[1].set_ylim(-2.4,2.4)


ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')

plt.tight_layout()
plt.savefig('Figures/active_traj_tmax_1.pdf')
plt.show()