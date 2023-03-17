import numpy as np
from kep2car import kep2car
from scipy.integrate import odeint
from tbp_ode import tbp_ode

'''
    GroundTrack.py - computes the ground track of an orbit in the unperturbed 2BP

    Prototype: alpha, delta, lon, lat = GroundTrack(s0, lon0, t, muP, wP, s)

    INPUTS:
            s0 [6 x 1] State of the orbit at the initial time (either in Cartesian or Keplerian elements) 
            lon0 [1 x 1] Longitude of Greenwich meridian at initial time
            t [n x 1] Vector of times at which the ground track will be computed
            wP [1 x 1] Planet's Rotational velocity
            s [1 x 1] s=1 if s0 is Cartesian form, s=2 if s0 is in Keplerian form

    OUTPUTS
            alpha [1 x 1] right ascension in Earth Centred Equatorial Inertial frame
            delta [1 x 1] declination in Earth Centred Equatorial Inertial frame
            lon [1 x 1] longitude with respect to rotating Earth 0degat Greenwich meridian
            lat [1 x 1] latitude with respect to rotating Earth

    AUTHOR: Giovanni Facchinetti, 2023
'''


def GroundTrack(s0, lon0, t, muP, wP, s):

    # checking if the state vector is in Keplerian form
    if s == 2:
        r0, v0 = kep2car(s0[0], s0[1], s0[2], s0[3], s0[4], s0[5], muP)

    else:
        r0 = s0[:3]
        v0 = s0[3:]

    y0 = np.concatenate((r0, v0))

    # Reshape y0 into a 1D array using ravel() function
    y0 = np.ravel(y0)

    # orbit propagation
    options = {'rtol': 1e-13, 'atol': 1e-13}
    Y = odeint(tbp_ode, y0, np.ravel(t), args=(muP,), atol=options['atol'], rtol=options['rtol'])
    r = Y[:, :3]
    v = Y[:, 3:]
    k = len(r)

    # Computation of the parameters
    r_norm = np.zeros(k)
    v_norm = np.zeros(k)
    delta = np.zeros(k)
    alpha = np.zeros(k)
    lonG = np.zeros(k)
    lon = np.zeros(k)
    lat = np.zeros(k)

    for i in np.arange(k):
        r_norm[i] = np.linalg.norm(r[i, :])
        v_norm[i] = np.linalg.norm(v[i, :])

        # Declination
        delta[i] = np.arcsin(r[i, 2] / r_norm[i])

        # Right Ascension
        if (r[i, 1] / r_norm[i]) > 0:
            alpha[i] = np.arccos((r[i, 0] / r_norm[i]) / np.cos(delta[i]))
        else:
            alpha[i] = 2 * np.pi - np.arccos((r[i, 0] / r_norm[i]) / np.cos(delta[i]))

        # longitude
        lonG[i] = lon0 + wP * (t[i] - t[0])
        lon[i] = alpha[i] - lonG[i]

        # latitude
        lat[i] = delta[i]

    return alpha, delta, lon, lat
