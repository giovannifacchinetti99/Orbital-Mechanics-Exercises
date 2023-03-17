import numpy as np
'''
    tbp_ode.py - returns state vector of velocity and acceleration of a point in an orbit in the perturbed 2BP
    
    Prototype: dy = tbp_ode(y, t, muP, Re, j2)
    
    INPUT: 
           y [1x6] vector containing the position and the velocity of the point of the orbit in cartesian coordinates [km, km/s]       
           t [1x1] instant of time [s]                                                             
           muP [1x1]  Planetary constant of the planet [km^3/s^2]                     
           Re [1x1] Radius of the Earth [km]                                                 
           j2 [1x1] Second zonal harmonic of the gravitational perturbation [-]                     
           
    OUTPUT: 
            dy: vector containing velocity and acceleration of the point, to be integrated  [1x6]
    
    AUTHOR: Giovanni Facchinetti, 2023
'''

def tbp_ode2(y, t, muP, Re, j2):

    # position and velocity
    r = y[:3]
    v = y[3:]

    r_norm = np.linalg.norm(r)

    aj2 = ((1.5 * (j2 * muP * (Re ** 2)) / (r_norm ** 4))
           * (((y[0] / r_norm) * (5 * ((y[2] ** 2) / (r_norm ** 2)) - 1) * np.array([1, 0, 0]))
              + ((y[1] / r_norm) * (5 * ((y[2] ** 2) / (r_norm ** 2)) - 1) * np.array([0, 1, 0]))
              + ((y[2] / r_norm) * (5 * ((y[2] ** 2) / (r_norm ** 2)) - 3) * np.array([0, 0, 1]))))

    dy = np.concatenate((v, (-muP / (r_norm ** 3)) * r + aj2))

    return dy


