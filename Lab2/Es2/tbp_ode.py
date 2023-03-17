import numpy as np
'''
    tbp_ode.py - returns state vector of velocity and acceleration of a point in an orbit in the unperturbed 2BP

    Prototype: dy = tbp_ode(y, t, muP)

    INPUT: 
            y [1 x 6]  state vector in cartesian coordinates [km, km/s]
            t [1 x 1]  instant of time [s]
            muP [1 x 1] Planetary constant of the planet [km^3/s^2]
       
    OUTPUT: 
            dy [1 x 6] vector containing velocity and acceleration of the point, to be integrated [km/s, km/s^2]

    AUTHOR: Giovanni Facchinetti, 2023
'''
def tbp_ode(y, t, muP):

    # position and velocity
    r = y[:3]
    v = y[3:]

    r_norm = np.linalg.norm(r)

    # value of the derivative vector
    a = (-muP / r_norm ** 3) * r
    dy = np.concatenate((v, a))

    return dy
