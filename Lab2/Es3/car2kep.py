import numpy as np

'''
    car2kep.py - Conversion from Cartesian elements to Keplerian coordinates

    Prototype: r,v = car2kep(a, e, i, OM, om, th, mu)

    INPUT: 
             r [3 x 1] Position vector [km]
             v [3 x 1] Velocity vector [km/s]
             mu [1 x 1] Gravitational parameter [km^3/s^2]

    OUTPUT:
             a  [1 x 1] Semi major axis [km]
             e  [1 x 1] Eccentricity [-]
             i  [1 x 1] Inclination [rad]
             OM [1 x 1] RAAN [rad]
             om [1 x 1] Pericentre anomaly [rad]
             th [1 x 1] True anomaly [rad]
             
    Author: Giovanni Facchinetti, 2023

'''
def car2kep(r, v, mu):

    # Calculate the norm of r
    r_norm = np.linalg.norm(r)

    # Calculate the norm of v
    v_norm = np.linalg.norm(v)

    # Calculate the specific angular momentum
    h = np.cross(r, v)

    # Calculate the magnitude of the specific angular momentum
    h_norm = np.linalg.norm(h)

    # Calculate the inclination
    # Calculate the z-component of h, i.e., hz
    h_z = h[2]

    # Calculate the inclination
    i = np.arccos(h_z/h_norm)

    # Calculate the eccentricity vector
    e = 1/mu * (((v_norm)**2 - (mu/r_norm))*r - np.dot(r, v)*v)

    # Calculate the magnitude of e
    e_norm = np.linalg.norm(e)

    # Calculate the specific mechanical energy
    E = 0.5*(v_norm)**2 - (mu/r_norm)

    # Calculate the semi-major axis
    a = -(mu/(2*E))

    # Calculate the line of nodes
    # Define the unit vector K
    K = np.array([0, 0, 1])

    # Calculate the vector of the line of nodes
    N = np.cross(K, h)

    # Calculate the norm of N
    N_norm = np.linalg.norm(N)

    # Calculate the right ascension of the ascending node (OM)
    # Calculate the Nx and Ny components
    N_x = N[0]
    N_y = N[1]

    # Calculate the right ascension of the ascending node (OM)
    # Use an if statement to avoid ambiguity due to arccos
    if N_y >= 0:
        OM = np.arccos(N_x/N_norm)
    else:
        OM = 2*np.pi - np.arccos(N_x/N_norm)

    # Calculate the argument of pericenter
    # Extract the e_z component
    e_z = e[2]

    # Calculate the argument of pericenter (om)
    # Use an if statement to avoid ambiguity due to arccos
    if e_z >= 0:
        om = np.arccos(np.dot(N, e)/(N_norm*e_norm))
    else:
        om = 2*np.pi - np.arccos(np.dot(N, e)/(N_norm*e_norm))

    # Calculate the radial velocity
    v_r = np.dot(r, v)/r_norm

    # compute true anomaly
    if v_r >= 0:
        th = np.acos(np.dot(e, r) / (e_norm * r_norm))
    else:
        th = 2 * np.pi - np.acos(np.dot(e, r) / (e_norm * r_norm))

    return a, e, i, OM, om, th