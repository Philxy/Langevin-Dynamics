import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib

directoryV04 = 'ActiveTrajV04/'
directoryV00 = 'ActiveTrajV04/'



plt.figure(figsize=(12/2.54, 8/2.54), dpi=80)

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
        x.append(float(row[1]))
        y.append(float(row[2]))

    plt.plot(x,y, label=label)

    '''
    x_max = max(np.abs(x))
    y_max = max(np.abs(y))
    size = np.max([y_max, x_max])
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    '''

plt.xlabel('x')
plt.ylabel('y')
plt.legend(title='$v_0$')
plt.tight_layout()
plt.savefig('Figures/active_traj.pdf')
plt.show()