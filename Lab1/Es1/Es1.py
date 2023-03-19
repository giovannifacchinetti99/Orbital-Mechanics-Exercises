import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from tbp_ode import tbp_ode
from astroConstants import astroConstants
from plot_planet import plot_planet

# ORBIT PROPAGATION
muP = astroConstants([13])  # [km^3/s^2]
n = 5  # number of orbits

# Initial conditions
r0 = np.array([6495, -970, -3622])  # [km]
v0 = np.array([4.752, 2.130, 7.950])  # [km/s]
y0 = np.concatenate((r0, v0))

# norm of r0
r0_norm = np.linalg.norm(r0)  # [km]

# time
a = 1 / (2 / r0_norm - np.dot(v0, v0) / muP)  # semi-major axis [km]
T = 2 * np.pi * np.sqrt((a ** 3) / muP)  # Period of the orbit [s]
t = np.linspace(0, n*T, 100000)

# integration
options = {'rtol': 1e-13, 'atol': 1e-13}
Y = odeint(tbp_ode, y0, np.ravel(t), args=(muP,), atol=options['atol'], rtol=options['rtol'])

# ANALYSIS OF THE RESULTS
r = Y[:, :3]
v = Y[:, 3:]
k = len(r)

# specific energy
eps = np.zeros(k)
for i in np.arange(k):
    eps[i] = (np.linalg.norm(v[i, :]) ** 2) / 2 - muP / np.linalg.norm(r[i, :])

# angular momentum
h = np.zeros((k, 3))
h_norm = np.zeros(k)
for i in np.arange(k):
    h[i, :] = np.cross(r[i, :], v[i, :])
    h_norm[i] = np.linalg.norm(h[i])

# eccentricity vector
e = np.zeros((k, 3))
e_norm = np.zeros(k)
for i in np.arange(k):
    e[i, :] = ((1 / muP) * np.cross(v[i, :], h[i, :])) - (r[i, :] / np.linalg.norm(r[i, :]))
    e_norm[i] = np.linalg.norm(e[i, :])

# true anomaly
f = np.zeros(k)
for i in np.arange(k):
    # from Laplace Method
    f[i] = np.arctan2(np.dot(np.cross(e[i, :], r[i, :]), h[i, :]), np.dot(r[i, :], e[i, :]) * np.linalg.norm(h[i, :]))
    if f[i] < 0:
        f[i] += 2 * np.pi

# Radial velocity
vr = np.zeros(k)
for i in np.arange(k):
    vr[i] = (muP / np.linalg.norm(h[i, :])) * np.linalg.norm(e[i, :]) * np.sin(f[i])

# Transverse velocity
vth = np.zeros(k)
for i in np.arange(k):
    vth[i] = (muP / np.linalg.norm(h[i, :])) * (1 + (np.linalg.norm(e[i, :]) * np.cos(f[i])))

# PLOTTING THE RESULTS
fig = plt.figure(figsize=(13, 18))

# Plot the orbit
ax1 = fig.add_subplot(2, 3, 1, projection='3d')

# Plot the trajectory
ax1.plot(r[:, 0], r[:, 1], r[:, 2], 'r', label='Trajectory')
plot_planet('earth', ax1)
ax1.axis('equal')
ax1.legend()
ax1.set_xlabel('$r_x$ [$10^3$ km]')
ax1.set_ylabel('$r_y$ [$10^3$ km]')
ax1.set_zlabel('$r_z$ [$10^3$ km]')
ax1.set_title('Orbit of spacecraft')
ax1.grid()
ax1.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))  # set scientific notation

# Plot the energy
ax2 = fig.add_subplot(2, 3, 2)
ax2.plot(t, eps)
ax2.set_title('energy and time')
ax2.set_xlabel('time [s]')
ax2.set_ylabel('energy [-]')
ax2.legend()
ax2.grid()
ax2.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))

# Plot the angular momentum
ax3 = fig.add_subplot(2, 3, 3)
ax3.plot(t, h[:, 0], label='$h_x$')
ax3.plot(t, h[:, 1], label='$h_y$')
ax3.plot(t, h[:, 2], label='$h_z$')
ax3.plot(t, h_norm, label='$||h||$')
ax3.set_title('angular momentum and time')
ax3.set_xlabel('time [s]')
ax3.set_ylabel('$h_x$, $h_y$, $h_z$, $||h||$ [km$^2$/s]')
ax3.legend()
ax3.grid()
ax3.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))

# Plot the eccentricity
ax4 = fig.add_subplot(2, 3, 4)
ax4.plot(t, e[:, 0], label='$e_x$')
ax4.plot(t, e[:, 1], label='$e_y$')
ax4.plot(t, e[:, 2], label='$e_z$')
ax4.plot(t, e_norm, label='$||e||$')
ax4.set_title('eccentricity and time')
ax4.set_xlabel('time [s]')
ax4.set_ylabel('$e_x$, $e_y$, $e_z$, $||e||$ [-]')
ax4.legend()
ax4.grid()
ax4.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))

# Plot the true anomaly
f = np.degrees(f)
ax5 = fig.add_subplot(2, 3, 5)
ax5.plot(t, f)
ax5.set_title('true anomaly and time')
ax5.set_xlabel('time [s]')
ax5.set_ylabel('true anomaly [deg]')
ax5.legend()
ax5.grid()
ax5.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))

# Plot transverse and radial velocities
ax6 = fig.add_subplot(2, 3, 6)
ax6.plot(t, vr, label='$v_r$')
ax6.plot(t, vth, label='$v_t$')
ax6.set_title('transverse and radial velocities and time')
ax6.set_xlabel('time [s]')
ax6.set_ylabel('transverse and radial velocities [km/s]')
ax6.legend()
ax6.grid()
ax6.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))

# Add spacing between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.3)

plt.show()

# Save the image in high resolution
fig.savefig('Es1.png', dpi=600)
