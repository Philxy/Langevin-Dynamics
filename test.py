import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-.7, 1.8, 10000)


plt.figure(figsize=(12/2.54,8/2.54))

def U(x):
    return .5 * x*x * ( 1-2*x/3)

plt.plot(x, U(x))
#plt.grid(visible=True, which='major', axis='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')


plt.xlabel('$x/x_{max}$')
plt.ylabel(r'$U(x)$')
plt.text(1.03, 1.0/6/2, r'$\Delta U$', color='tab:orange')
plt.vlines(x=1, ymin=0,ymax=1.0/6, color='tab:orange')
plt.scatter([0],[0], color='black')
plt.tight_layout()
plt.savefig('Figures/potential.pdf')
plt.show()