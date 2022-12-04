import matplotlib.pyplot as plt
import numpy as np




x = np.linspace(0,1000,10000)


kBT = 1
eta = 0.1
a = 1
D_T = kBT/(6*np.pi*eta*a)
D_R = kBT/(8*np.pi*eta*a*a*a)


def rr(x, v0, D_T, D_R):
    return (4 * D_T + 2* v0*v0 / D_R) * x + 2*v0*v0/(D_R*D_R) * (np.exp(-x*D_R)-1)

plt.plot(x,rr(x, 0, D_T, D_R))
plt.plot(x,rr(x, 50, D_T, D_R))
plt.plot(x, 4*D_T*x)

plt.xscale('log')
plt.yscale('log')
plt.show()