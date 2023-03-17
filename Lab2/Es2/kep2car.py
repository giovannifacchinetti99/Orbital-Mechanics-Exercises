import numpy as np
'''
    kep2car.py - Conversion from Keplerian elements to Cartesian coordinates
    
    Prototype: r,v = kep2car(a, e, i, OM, om, th, mu)
    
    INPUT: 
             a  [1 x 1] Semi major axis [km]
             e  [1 x 1] Eccentricity [-]
             i  [1 x 1] Inclination [rad]
             OM [1 x 1] RAAN [rad]
             om [1 x 1] Pericentre anomaly [rad]
             th [1 x 1] True anomaly [rad]
             mu [1 x 1] Gravitational parameter [km^3/s^2]
            
    OUTPUT
             r [3 x 1] Position vector [km]
             v [3 x 1] Velocity vector [km/s]
             
    Author: Giovanni Facchinetti, 2023

'''

def kep2car(a, e, i, OM, om, th, mu):

    # calculate p
    p = a * (1 - e**2)

    # calculate the norm of r in the perifocal frame
    r_norm_p = p / (1 + (e * np.cos(th)))

    # find r (vector) in the perifocal frame
    r_p = np.zeros((3, 1))
    r_p[0, 0] = r_norm_p * np.cos(th)
    r_p[1, 0] = r_norm_p * np.sin(th)
    r_p[2, 0] = 0

    # find v (vector) in the perifocal frame
    v_p = np.zeros((3, 1))
    molt = np.sqrt(mu / p)
    v_p[0, 0] = -molt * np.sin(th)
    v_p[1, 0] = molt * (e + np.cos(th))
    v_p[2, 0] = 0

    # rotate the state vector to the Geocentric Equatorial frame
    # define rotation matrices

    # Rotation matrix OM about k
    R1 = np.array([[np.cos(OM), np.sin(OM), 0],
                   [-np.sin(OM), np.cos(OM), 0],
                   [0, 0, 1]])

    # Rotation matrix i about i'
    R2 = np.array([[1, 0, 0],
                   [0, np.cos(i), np.sin(i)],
                   [0, -np.sin(i), np.cos(i)]])

    # Rotation matrix om about k''
    R3 = np.array([[np.cos(om), np.sin(om), 0],
                   [-np.sin(om), np.cos(om), 0],
                   [0, 0, 1]])

    # rotate the vectors to the Geocentric Equatorial frame
    T = np.dot(R3, np.dot(R2, R1))
    T_transp = T.T

    # calculate r (vector, Equatorial plane)
    r = np.dot(T_transp, r_p)

    # calculate v (vector, Equatorial plane)
    v = np.dot(T_transp, v_p)

    return r, v
