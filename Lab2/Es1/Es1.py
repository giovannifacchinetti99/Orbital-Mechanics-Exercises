import numpy as np
from astroConstants import astroConstants
import matplotlib.pyplot as plt
from GroundTrack import GroundTrack

# define data
muP = astroConstants([13])  # [km^2/s^3]
RP = astroConstants([23])  # [km]
wP = np.deg2rad(15.04)/3600  # Planet's Rotational velocity (15.04°/h) [rad/s]

# case 1: generic orbit
a_1 = 8350  # [km]
e_1 = 0.19760  # [-]
i_1 = np.deg2rad(60)  # [rad]
OM_1 = np.deg2rad(270)  # [rad]
om_1 = np.deg2rad(45)  # [rad]
f0_1 = np.deg2rad(230)  # [rad]

s0_1 = np.ndarray(shape=(6,), dtype=object)
s0_1[0] = a_1
s0_1[1] = e_1
s0_1[2] = i_1
s0_1[3] = OM_1
s0_1[4] = om_1
s0_1[5] = f0_1

# samples
k = 100000

# defining initial longitude
lon0_1 = 0

# time
n_orbits_1 = 3.25  # [-]
T_1 = 2 * np.pi / np.sqrt(muP / a_1**3)  # [s]
t_1 = np.linspace(0, n_orbits_1 * T_1, k)  # [s]

# computing the parameters
alpha_1, delta_1, lon_1, lat_1 = GroundTrack(s0_1, lon0_1, t_1, muP, wP, 2)

# Wrapping longitude between -pi and pi, and converting from radiant to degrees
for i in np.arange(k):
    lon_1[i] = lon_1[i] % (2*np.pi)
    if lon_1[i] > np.pi:
        lon_1[i] = lon_1[i] - 2*np.pi
    lon_1[i] = np.rad2deg(lon_1[i])
    lat_1[i] = np.rad2deg(lat_1[i])

# case 2: Molniya orbit
a_2 = 26600  # [km]
e_2 = 0.74  # [-]
i_2 = np.deg2rad(63.4)  # [rad]
OM_2 = np.deg2rad(50)  # [rad]
om_2 = np.deg2rad(280)  # [rad]
f0_2 = np.deg2rad(0)  # [rad]

s0_2 = np.ndarray(shape=(6,), dtype=object)
s0_2[0] = a_2
s0_2[1] = e_2
s0_2[2] = i_2
s0_2[3] = OM_2
s0_2[4] = om_2
s0_2[5] = f0_2

lon0_2 = 0

# time
n_orbits_2 = 30  # [-]
T_2 = 2 * np.pi / np.sqrt(muP / a_2**3)  # [s]
t_2 = np.linspace(0, n_orbits_2 * T_2, k)  # [s]

# computing the parameters
alpha_2, delta_2, lon_2, lat_2 = GroundTrack(s0_2, lon0_2, t_2, muP, wP, 2)

# Wrapping longitude between -pi and pi, and converting from radiant to degrees
for i in np.arange(k):
    lon_2[i] = lon_2[i] % (2*np.pi)
    if lon_2[i] > np.pi:
        lon_2[i] = lon_2[i] - 2*np.pi
    lon_2[i] = np.rad2deg(lon_2[i])
    lat_2[i] = np.rad2deg(lat_2[i])

# case 3: Three circular LEO orbits with 3 different inclinations
a_3 = 7171.010  # [km]
e_3 = 0  # [-]
i_3 = [np.deg2rad(0), np.deg2rad(30), np.deg2rad(98)]  # [rad]
OM_3 = np.deg2rad(0)  # [rad]
om_3 = np.deg2rad(40)  # [rad]
f0_3 = np.deg2rad(0)  # [rad]

s0_3 = np.ndarray(shape=(3, 6), dtype=object)
alpha_3 = np.ndarray(shape=(3, k), dtype=object)
delta_3 = np.ndarray(shape=(3, k), dtype=object)
lon_3 = np.ndarray(shape=(3, k), dtype=object)
lat_3 = np.ndarray(shape=(3, k), dtype=object)

for j in np.arange((len(i_3))):
    s0_3[j, 0] = a_3
    s0_3[j, 1] = e_3
    s0_3[j, 2] = i_3[j]
    s0_3[j, 3] = OM_3
    s0_3[j, 4] = om_3
    s0_3[j, 5] = f0_3

    lon0_3 = 0

    # time
    n_orbits_3 = 5
    T_3 = 2 * np.pi / np.sqrt(muP / a_3**3)
    t_3 = np.linspace(0, n_orbits_3 * T_3, k)

    # computing the parameters
    alpha_3[j, :], delta_3[j, :], lon_3[j, :], lat_3[j, :] = GroundTrack(s0_3[j, :], lon0_3, t_3, muP, wP, 2)

    # Wrapping longitude between -pi and pi, and converting from radiant to degrees
    for i in np.arange(k):
        lon_3[j, i] = lon_3[j, i] % (2*np.pi)
        if lon_3[j, i] > np.pi:
            lon_3[j, i] = lon_3[j, i] - 2*np.pi
        lon_3[j, i] = np.rad2deg(lon_3[j, i])
        lat_3[j, i] = np.rad2deg(lat_3[j, i])

# plot the result
im = plt.imread('BlueMarble.png')  # creating a as a matrix of colored pixels from the image
fig = plt.figure(figsize=(19.2, 10.8))

# define markersizes
g = 1
t = 5

# first orbit
ax1 = fig.add_subplot(2, 3, 1)
ax1.imshow(im, extent=[-180, 180, -90, 90])
ax1.plot(lon_1, lat_1, '.', markersize=g)
ax1.plot(lon_1[0], lat_1[0], 'o', markersize=t)
ax1.plot(lon_1[-1], lat_1[-1], 's', markersize=t)
ax1.set_xlim([-180, 180])
ax1.set_ylim([-90, 90])
ax1.grid(True)
ax1.set_title('Orbit 1')
ax1.legend(['ground track', 'start', 'finish'], loc='upper center', bbox_to_anchor=(0.5, 1.5), ncol=3)
ax1.set_xlabel('Longitude [deg]')
ax1.set_ylabel('Latitude [deg]')

# Molniya Orbit
ax2 = fig.add_subplot(2, 3, 2)
ax2.imshow(im, extent=[-180, 180, -90, 90])
ax2.plot(lon_2, lat_2, '.', markersize=g)
ax2.plot(lon_2[0], lat_2[0], 'o', markersize=t)
ax2.plot(lon_2[-1], lat_2[-1], 's', markersize=t)
ax2.set_xlim([-180, 180])
ax2.set_ylim([-90, 90])
ax2.grid(True)
ax2.set_title('Molniya Orbit')
ax2.legend(['ground track', 'start', 'finish'], loc='upper center', bbox_to_anchor=(0.5, 1.5), ncol=3)
ax2.set_xlabel('Longitude [deg]')
ax2.set_ylabel('Latitude [deg]')

# LEO orbit with i = 0°
ax3 = fig.add_subplot(2, 3, 4)
ax3.imshow(im, extent=[-180, 180, -90, 90])
ax3.plot(lon_3[0, :], lat_3[0, :], '.', markersize=g)
ax3.plot(lon_3[0, 0], lat_3[0, 0], 'o', markersize=t)
ax3.plot(lon_3[0, -1], lat_3[0, -1], 's', markersize=t)
ax3.set_xlim([-180, 180])
ax3.set_ylim([-90, 90])
ax3.grid(True)
ax3.set_title('LEO orbit with i = 0°')
ax3.legend(['ground track', 'start', 'finish'], loc='upper center', bbox_to_anchor=(0.5, 1.5), ncol=3)
ax3.set_xlabel('Longitude [deg]')
ax3.set_ylabel('Latitude [deg]')

# LEO orbit with i = 30°
ax4 = fig.add_subplot(2, 3, 5)
ax4.imshow(im, extent=[-180, 180, -90, 90])
ax4.plot(lon_3[1, :], lat_3[1, :], '.', markersize=g)
ax4.plot(lon_3[1, 0], lat_3[1, 0], 'o', markersize=t)
ax4.plot(lon_3[1, -1], lat_3[1, -1], 's', markersize=t)
ax4.set_xlim([-180, 180])
ax4.set_ylim([-90, 90])
ax4.grid(True)
ax4.set_title('LEO orbit with i = 30°')
ax4.legend(['ground track', 'start', 'finish'], loc='upper center', bbox_to_anchor=(0.5, 1.5), ncol=3)
ax4.set_xlabel('Longitude [deg]')
ax4.set_ylabel('Latitude [deg]')

# LEO orbit with i = 98°
ax5 = fig.add_subplot(2, 3, 6)
ax5.imshow(im, extent=[-180, 180, -90, 90])
ax5.plot(lon_3[2, :], lat_3[2, :], '.', markersize=g)
ax5.plot(lon_3[2, 0], lat_3[2, 0], 'o', markersize=t)
ax5.plot(lon_3[2, -1], lat_3[2, -1], 's', markersize=t)
ax5.set_xlim([-180, 180])
ax5.set_ylim([-90, 90])
ax5.grid(True)
ax5.set_title('LEO orbit with i = 98°')
ax5.legend(['ground track', 'start', 'finish'], loc='upper center', bbox_to_anchor=(0.5, 1.5), ncol=3)
ax5.set_xlabel('Longitude [deg]')
ax5.set_ylabel('Latitude [deg]')

# Add spacing between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.3)

# Save the image in high resolution
fig.savefig('Es1.png', dpi=600)

plt.show()