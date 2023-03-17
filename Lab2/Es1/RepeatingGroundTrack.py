import numpy as np

'''
    RepeatingGroundTrack.py - computes the required semi-major axis for a repeating ground track with 𝑘 satellite 
    revolutions and 𝑚 Earth revolutions in the unperturbed 2BP

    Prototype: a = RepeatingGroundTrack(k, m, muP, wP)

    INPUTS:
            m [1 x 1] rotations of the planet before the track repeats itself [-] 
            k [1 x 1] revolutions of the satellite before the track repeats itself [-]
            muP [1 x 1] gravitational planetary constant [km^3/s^2]
            wP [1 x 1] rotational velocity of the planet [rad/s]
      
    OUTPUTS
            a [1 x 1] semi-major axis of the orbit [km]
            
    AUTHOR: Giovanni Facchinetti, 2023
'''


def RepeatingGroundTrack(k, m, muP, wP):
    T = (2 * np.pi * m) / (wP * k)  # Period of the orbit

    a = (((T ** 2) * muP) / (4 * (np.pi ** 2))) ** (1 / 3)  # Semi-major axis

    return a
