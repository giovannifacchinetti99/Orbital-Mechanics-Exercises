import matplotlib.pyplot as plt
from astroConstants import astroConstants
import numpy as np
from Kepler_Solver import Kepler_Solver

# initializing the problem

a = 7000  # semi-major axis [km]
muP = astroConstants([13])  # planetary constant [km^3/s^2]
t0 = 0  # [s]
e = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.95, 0.99])  # eccentricity array [-]
n = np.sqrt(muP / a ** 3)  # mean motion [rad/s]
T = 2*np.pi/n  # period [s]
k = 2  # number of revolutions
N = 10000  # samples of time
t = np.linspace(t0, k*T, N)


# computing the true anomalies

f_vec = np.zeros((N, len(e)))
for i in np.arange(N):
    for j in np.arange(len(e)):
        f_vec[i, j] = Kepler_Solver(t[i], e[j], a, muP, t0)
        f_vec[i, j] = np.rad2deg(f_vec[i, j])

# plotting the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the face colors based on the z-values
# t/T is performed for a better visualization in the label cmap='jet' map the surface from blue to yellow;
surf = ax.plot_surface(t/T, e, f_vec, cmap='jet')

ax.legend()
ax.set_xlabel('$t$ [T]')
ax.set_ylabel('$e$ [-]')
ax.set_zlabel('$f$ [deg]')
ax.set_title('Evolution of true anomaly with time and eccentricity')
ax.grid()
plt.show()
fig.savefig('Es3.png', dpi=600)

