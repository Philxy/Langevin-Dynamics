import csv
import matplotlib.pyplot as plt
import numpy as np
import os


directory = 'MSDs/'


def rr(x, v0, D_T, D_R):
    return (4 * D_T + 2* v0*v0 / D_R) * x + 2*v0*v0/(D_R*D_R) * (np.exp(-x*D_R)-1)

plt.figure(figsize=(12/2.54, 8/2.54), dpi=80)

times = []
MSDs = []
labels = []

for i, filename in enumerate(os.listdir(directory)):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []
    MSD_t = []
    v0_str = (filename.split('.')[0])
    labels.append(v0_str)

    for row in csvreader:
        time.append(float(row[0]))
        MSD_t.append(float(row[1]))

    times.append(time)
    MSDs.append(MSD_t)


x = np.linspace(0.00, 100, 10000)


for i in range(len(labels)):
    plt.plot(times[i], MSDs[i], label=labels[i])

    kBT = 0.1
    a = 0.1
    eta = 1.0087
    D_T = kBT / (6*np.pi*eta*a)
    D_R = kBT / (6*np.pi*eta*a**3)

    plt.plot(time, [rr(t, float(labels[i]), D_T=D_T, D_R=D_R) for t in time], linestyle=':', label=labels[i])
    


plt.xscale('log')
plt.yscale('log')
plt.legend(title='$v_0$')
plt.show()