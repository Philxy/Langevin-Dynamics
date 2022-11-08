import csv
import matplotlib.pyplot as plt
import numpy as np
import os

directory = 'MSDs/'


kBT = 1.0
friction = 1.0
m = 1.0


MSD_sum = [0] * 200000

n = 0

for i, filename in enumerate(os.listdir(directory)):

    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []
    MSD = []
    n += 1.0

    for row in csvreader:
        time.append(float(row[0]))

        MSD.append(float(row[1]))

    for m, x in enumerate(MSD):
        MSD_sum[m] += x



    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.plot(time, [4.0 * kBT / friction * t for t in time], linestyle=':', label=r'Theorie $\langle \Delta\mathbf{r}(t)^2\rangle = 4 k_B T t / \lambda$')
    plt.xlabel('Zeit t')
    plt.ylabel(r'MSD $\langle \Delta\mathbf{r}(t)^2\rangle$')
    plt.plot(time, [m/n for m in MSD_sum], label='Simulation')
    plt.ylim(-50,450)
    plt.yticks([0,10000,20000,30000,40000])
    plt.title('Anzahl Trajektorien N = ' + str(i))
    plt.legend(loc='upper left')
    plt.savefig('FramesMSD/' + str(i) + '.png')
    plt.clf()


os.system(
    "ffmpeg -r 20 -i FramesMSD/%01d.png -vcodec mpeg4 -y -vb 40M MSD_averaging3.mp4")
