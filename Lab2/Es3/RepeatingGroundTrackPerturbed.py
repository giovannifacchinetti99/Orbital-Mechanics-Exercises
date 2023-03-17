import numpy as np
from scipy.optimize import fsolve
from car2kep import car2kep
from astroConstants import astroConstants

'''
    RepeatingGroundTrackPerturbed.py - computes the required semi-major axis for a repeating ground track with 𝑘 satellite 
    revolutions and 𝑚 Earth revolutions in the perturbed 2BP under the effect of the J2 perturbation

    Prototype: a = RepeatingGroundTrackPerturbed(s0, k, m, muP, wP, J2, s)

    INPUTS:
            s0 [6 x 1] state vector both in cartesian or keplerian form
            m [1 x 1] rotations of the planet before the track repeats itself [-] 
            k [1 x 1] revolutions of the satellite before the track repeats itself [-]
            muP [1 x 1] gravitational planetary constant [km^3/s^2]
            wP [1 x 1] rotational velocity of the planet [rad/s]
            J2 [1 x 1] second zonal harmonic of the Earth's oblateness [-]
            s [1 x 1] if s=1: s0 is in cartesian form, if s=2: s0 is in keplerian form


    OUTPUTS
            a [1 x 1] semi-major axis of the orbit [km]

    AUTHOR: Giovanni Facchinetti, 2023
'''

# constants
Re = astroConstants([23])  # [km]

def RepeatingGroundTrackPerturbed(s0, k, m, muP, wP, J2, s):
    if s == 1:  # s is in cartesian form
        (a, e, i, OM, om, th) = car2kep(s0[:3], s0[3:], muP)

    else:
        a = s0[0]
        e = s0[1]
        i = s0[2]

    n = lambda x: np.sqrt(muP / (x ** 3))  # mean motion

    # define secular evolution for OM, om, M
    if e != 0:
        A = lambda x: ((3 * np.sqrt(muP) * J2 * (Re ** 2)) / (2 * ((1 - (e ** 2)) ** 2) * (x ** (7 / 2))))
        M0_sec = lambda x: ((3 * np.sqrt(muP) * J2 * (Re ** 2)) / (2 * ((1 - (e ** 2)) ** 1.5) * (x ** (7 / 2)))) * (
                    1 - (1.5 * (np.sin(i) ** 2)))
    else:
        A = lambda x: ((3 * np.sqrt(muP) * J2 * (Re ** 2)) / (2 * (x ** (7 / 2))))
        M0_sec = lambda x: ((3 * np.sqrt(muP) * J2 * (Re ** 2)) / (2 * (x ** (7 / 2)))) * (1 - (1.5 * (np.sin(i) ** 2)))

    OM_sec = lambda x: -A(x) * np.cos(i)
    om_sec = lambda x: -A(x) * ((2.5 * ((np.sin(i)) ** 2) - 2))

    # define function input of fsolve
    fun = lambda x: (wP - OM_sec(x)) / (n(x) + om_sec(x) + M0_sec(x)) - m / k

    # find the zero
    x = fsolve(fun, a)
    a = x
    return a
