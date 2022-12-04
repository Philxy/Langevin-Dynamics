import csv
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import stats
import scipy.integrate as integrate
from mpl_toolkits import mplot3d

def U(x,y):
    A = .5
    omega = 2
    return A* np.cos(omega * np.pi*x)  +  A * np.cos(omega * np.pi*y) 


x = np.linspace(0,1, 60)
y = np.linspace(0,1, 60)
X, Y = np.meshgrid(x, y)
Z = U(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plane = X * 0 + .5
ax.plot_surface(plane, Y, 2*X-1.25, alpha=0.8)
ax.set_xlabel('$x/L$')
ax.set_ylabel('$y/L$')
ax.set_zlabel('$U(x,y)$')
#ax.set_xlim(.25,.75)
#ax.set_ylim(.25,.75)

# Rotate the axes and update
for angle in range(0, 360 + 1, 2):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    azim = roll = 0
    elev = 30
    if angle <= 360:
        azim = angle_norm
    else:
         azim = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)

    plt.draw()
    plt.savefig('Frames2/' + str(angle) + '.png')


plt.show()
plt.clf()



plt.figure(figsize=(16/2.54, 6/2.54), dpi=80)

f, ax1 = plt.subplots(figsize=(10/2.54, 8/2.54))

directory = 'MSDs/'


diffusion_coeffs = []
kBTs = []

colors = plt.cm.plasma(np.linspace(0,1,5))

for i, filename in enumerate(sorted(os.listdir(directory))):
    path = os.path.join(directory, filename)
    # checking if it is a file
    if not os.path.isfile(path):
        continue

    csvreader = csv.reader(open(path, 'r'))
    time = []
    MSD = []
    kBT = float(filename.replace('.csv', ''))

    for row in csvreader:
        t = float(row[0])
        if t < 1:
            continue
        time.append(t)
        MSD.append(float(row[1]))

    plt.plot(time,MSD,label=str(kBT), color=colors[i])
    

    res = stats.linregress(time, MSD)
    D = res.slope / (4.0)
    diffusion_coeffs.append(D)
    kBTs.append(kBT)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Zeit $t$')
plt.ylabel(r'MSD $\langle x^2(t) \rangle$')
plt.legend(title='$k_BT$')
plt.tight_layout()
plt.savefig('Figures/MSD_periodic.pdf')
plt.show()
plt.clf()

ax1.scatter(kBTs, diffusion_coeffs)


def U(x):
    y = .25
    return 0.5 * np.sin(2 * (np.pi*x)) #- 0.5 * np.sin(2 * (np.pi*y))


def integrand_plus(x,kBT):
    return np.exp(U(x)/kBT)


def integrand_minus(x,kBT):
    return np.exp(-U(x)/kBT)


D_eff = []

x = np.linspace(0.1, 100, 5000)

a = 0
b = 2

for kBT in x:
    integral_plus = integrate.quad(integrand_plus, a, b, args=(kBT))[0] / (b-a) 
    integral_minus = integrate.quad(integrand_minus, a, b, args=(kBT))[0] / (b-a)
    D0 = 4.0 * kBT / 1.0
    D_eff.append(D0/(integral_plus * integral_minus) / 10)


size = 4


ax1.plot(x, D_eff, linestyle=':')

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.set_xlabel('$k_BT$')
ax1.set_ylabel('Diffusionskoeffizient $D$')
plt.tight_layout()
plt.savefig('Figures/kbT_D.pdf')
plt.show()