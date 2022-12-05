import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib

directory = 'MSDs/'


def rr(x, v0, D_T, D_R):
    return (4 * D_T + 2* v0*v0 / D_R) * x + 2*v0*v0/(D_R*D_R) * (np.exp(-x*D_R)-1)

plt.figure(figsize=(12/2.54, 8/2.54), dpi=80)



times = []
MSDs = []
labels = []

for i, filename in enumerate(sorted(os.listdir(directory))):
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

norm = matplotlib.colors.Normalize(
    vmin=np.min([float(label) for label in labels]),
    vmax=np.max([float(label) for label in labels]))
c_m = matplotlib.cm.winter
s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
s_m.set_array([])


for i in range(len(labels)):
    plt.plot(times[i], MSDs[i], label=labels[i],color=s_m.to_rgba(float(labels[i])))

    kBT = 0.1
    a = 0.1
    eta = 1.0087
    D_T = kBT / (6*np.pi*eta*a)
    D_R = kBT / (6*np.pi*eta*a**3)

    plt.plot(time, [rr(t, float(labels[i]), D_T=D_T, D_R=D_R) for t in time], linestyle=':',color=s_m.to_rgba(float(labels[i])))



plt.plot(x[int(len(x)/100):], 100*x[int(len(x)/100):], color='grey')
plt.plot(x[int(len(x)/5000):int(len(x)/500)], 100*x[int(len(x)/5000):int(len(x)/500)] * x[int(len(x)/5000):int(len(x)/500)], color='grey')
plt.text(int(len(x)/5000), 300*int(len(x)/5000), r'$\propto t$')
plt.text(0.04, 1, r'$\propto t^2$')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Zeit t')
plt.ylabel(r'MSD $\langle \mathbf{r}^2(t) \rangle$')
plt.legend(title='$v_0$')
plt.tight_layout()
plt.savefig('Figures/active_MSD.pdf')
plt.show()