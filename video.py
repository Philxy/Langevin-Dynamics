import csv
import matplotlib.pyplot as plt
import numpy as np
import os


directory = 'trajectories/'

file = open('trajectories/trajectory0.csv')
csvreader = csv.reader(file)


x = []
y = []
time = []
for row in csvreader:
    time.append(float(row[0]))
    x.append(float(row[1]))
    y.append(float(row[2]))

size = 50


for i, count in enumerate(range(0, len(x), 200)):
    circle = plt.scatter(x[count], y[count], color='tab:blue', marker='o')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.xlim(-size,size)
    plt.ylim(-size,size)
    plt.plot(x[:count], y[:count])
    #plt.title('Zeit = ' + str(time[count]))
    plt.savefig('Frames/' + str(i) + '.png')
    plt.clf()



os.system("ffmpeg -r 20 -i FramesMSD/%01d.png -vcodec mpeg4 -y -vb 40M MSD_averaging.mp4")



