import numpy as np
import scipy as sp
from scipy.optimize import root

'''
 Kepler_Solver - finds true anomaly f starting from mean anomaly M
 
 Prototype: f =  Kepler_Solver(t, e, a, muP, f0, t0)
 
 Input:   time vector(t) [1 x n] [s]
          eccentricity (e) [-]
          semi-major axis (a) [km]
          Standard gravitational parameter (mu) [km^3/s^2]
          reference initial time and true anomaly (t0) [s]
          
 Output:  true anomaly (f) [rad]

 AUTHOR: Giovanni Facchinetti, 2023
'''


def Kepler_Solver(t, e, a, muP, t0):
    # define Mean Anomaly M
    n = np.sqrt(muP / a ** 3)
    M0 = 0
    M = M0 + n * (t - t0)

    # wrapping M
    M_wrap = M % (2 * np.pi)
    k = np.floor(M / (2 * np.pi))  # M = M_wrap + 2k*pi

    # find reduced Eccentric Anomaly using the Kepler's equation
    fun = lambda E: E - e * (np.sin(E)) - M_wrap
    guess = M_wrap + ((e * np.sin(M_wrap)) / (1 - np.sin(M_wrap + e) + np.sin(M_wrap)))
    sol = root(fun, guess)
    E = sol.x  # extracting the root from the solution object

    # computing the reduced true anomaly
    f_wrap = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))

    # unwrapping f_wrap
    f = f_wrap + 2 * k * np.pi

    return f
