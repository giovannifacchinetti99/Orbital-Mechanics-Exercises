import numpy as np

"""
 Returns astrodynamic-related physical constants.

 Args:
     in_vec (numpy.ndarray): vector of identifiers of required constants.

 Returns:
     out_vec (numpy.ndarray): vector of constants.

 List of identifiers:
 Generic astronomical constants:
     1   Universal gravity constant (G) (from DITAN and Horizon) [km^3/(kg*s^2)]
     2   Astronomical Unit (AU) (from DE405) [km]
         Note:  The value for 1 au is from the IAU 2012 Resolution B1.
 Sun related:
     3   Sun mean radius (from DITAN) [km]
     4   Sun planetary constant (mu = mass * G) (from DE405)
         [km^3/s^2]
     31  Energy flux density of the Sun (from Wertz,SMAD)
         [W/m2 at 1 AU]
 Other:
     5   Speed of light in the vacuum (definition in the SI and Horizon) [km/s]
     6   Standard free fall (the acceleration due to gravity on the
         Earth's surface at sea level) (from Wertz,SMAD) [m/s^2]
     7   Mean distance Earth-Moon (from Wertz,SMAD) [km]
     8   Obliquity (angle) of the ecliptic at Epoch 2000 (from
         Horizon) [rad]
     9   Gravitational field constant of the Earth (from Wertz,SMAD,
         taken from JGM-2). This should be used in conjunction to
         Earth radius = 6378.1363 km
     32  Days in a Julian year y = 365.25 d  (from Horizon)
 Planetary constants of the planets (mu = mass * G) [km^3/s^2]:
     11  Me      (from DE405)
     12  V       (from DE405)
     13  E       (from DE405)
     14  Ma      (from DE405)
     15  J       (from DE405)
     16  S       (from DE405)
     17  U       (from DE405)
     18  N       (from DE405)
     19  P       (from DE405)
     20  Moon    (from DE405)
 Mean radius of the planets [km]:
     21  Me      (from Horizon)
     22  V       (from Horizon)
     23  E       (from Horizon)
     24  Ma      (from Horizon)
     25  J       (from Horizon)
     26  S       (from Horizon)
     27  U       (from Horizon)
     28  N       (from Horizon)
     29  P       (from Horizon)
     30  Moon    (from Horizon)

 Notes for upgrading this function:
     It is possible to add new constants.
     - DO NOT change the structure of the function, as well as its
         prototype.
     - DO NOT change the identifiers of the constants that have already
         been defined in this function. If you want to add a new
         constant, use an unused identifier.
     - DO NOT add constants that can be easily computed starting form
         other ones (avoid redundancy).
     Contact the author for modifications.
"""

def astroConstants(in_):
        out = np.zeros(len(in_))
        for i in range(len(in_)):
            if in_[i] == 1:
                out[i] = 6.67259e-20  # From DITAN and Horizon
            elif in_[i] == 2:
                out[i] = 149597870.691  # From DE405
            elif in_[i] == 3:
                # out[i] = 700000  # From DITAN
                out[i] = 6.955 * 10 ** 5  # From Horizon [W3]
            elif in_[i] == 4:
                # out[i] = 0.19891000000000E+31*6.67259e-20  # From DITAN
                out[i] = 1.32712440017987E+11  # From DE405 [A]
            elif in_[i] == 5:
                out[i] = 299792.458  # Definition in the SI, Horizon, DE405
            elif in_[i] == 6:
                out[i] = 9.80665  # Definition in Wertz, SMAD
            elif in_[i] == 7:
                # out[i] = 384401  # Definition in Wertz, SMAD
                out[i] = 384400  # From Horizon [W3]
            elif in_[i] == 8:
                # out[i] = 23.43928111 * pi / 180  # Definition in Wertz, SMAD
                out[i] = 84381.412 / 3600 * np.pi / 180  # Definition in Horizon
                # obliquity of ecliptic (J2000)    epsilon = 84381.412 (± 0.005) arcsec
            elif in_[i] == 9:
                out[i] = 0.1082626925638815e-2  # Definition in Wertz, SMAD
            elif in_[i] == 11:
                # out[i] = 0.33020000000000E+24*6.67259e-20  # From DITAN
                # out[i] = 0.330104E+24*6.67259e-20  # From Horizon [F]
                out[i] = 2.203208E+4  # From DE405
            elif in_[i] == 12:
                # out[i] = 0.48685000000000E+25*6.67259e-20  # From DITAN
                # out[i] = 4.86732E+24*6.67259e-20  # From Horizon [G]
                out[i] = 3.24858599E+5  # From DE405
            elif in_[i] == 13:
                # out[i] = 0.59736990612667E+25*6.67259e-20  # From DITAN
                # out[i] = 5.97219E+24*6.67259e-20  # From Horizon [H]
                out[i] = 3.98600433e+5  # From DE405
            elif in_[i] == 14:
        # out[i] = 0.64184999247389E+24*6.67259e-20  # From DITAN
                out[i] = 4.2828314E+4
            elif in_[i] == 15:
                out[i] =  1.26712767863E+08
            elif in_[i] == 16:
                out[i] = 3.79406260630E+07
            elif in_[i] == 17:
                out[i] = 5.79454900700E+06
            elif in_[i] == 18:
                # out(i)=0.10243000000000E+27*6.67259e-20; % From DITAN
                # out(i)=102.410E+24*6.67259e-20;     % From Horizon [M]
                out[i] = 6.83653406400E+06  # From DE405
            elif in_[i] == 19:
                # out(i)=0.14120000000000E+23*6.67259e-20; % From DITAN
                #out(i)=.01309E+24*6.67259e-20;     % From Horizon [N]
                out[i] = 9.81601000000E+02  # From DE405
            elif in_[i] == 20:
                # out(i)=0.73476418263373E+23*6.67259e-20; % From DITAN
                out[i] = 4902.801  # From Horizon  [M2]
                #out(i)=4902.801076;                % From Horizon  [M3]
            elif in_[i] == 21:
                # out(i)=0.24400000000000E+04; % From DITAN
                out[i] = 2439.7  # From Horizon [D]
            elif in_[i] == 22:
                # out(i)=0.60518000000000E+04; % From DITAN
                out[i] = 6051.8  # From Horizon [D]
            elif in_[i] == 23:
                # out(i)=0.63781600000000E+04; % From DITAN
                # out(i)=6371.00; % From Horizon [B]
                out[i] = 6371.01  # From Horizon [W3]
            elif in_[i] == 24:
                # out(i)=0.33899200000000E+04; % From DITAN
                # out(i)=3389.50; % From Horizon [D]
                out[i] = 3389.9  # From Horizon [W3]
            elif in_[i] == 25:
                # out(i)=0.69911000000000E+05; % From DITAN
                out[i] = 69911  # From Horizon [D]
            elif in_[i] == 26:
                # out(i)=0.58232000000000E+05; % From DITAN
                out[i] = 58232  # From Horizon [D]
            elif in_[i] == 27:
                # out(i)=0.25362000000000E+05; % From DITAN
                out[i] = 25362  # From Horizon [D]
            elif in_[i] == 28:
                # out(i)=0.24624000000000E+05; % From DITAN
                # out(i)=24622;   % From Horizon [D]
                out[i] = 24624  # From Horizon [W3]
            elif in_[i] == 29:
                # out(i)=0.11510000000000E+04; % From DITAN
                out[i] = 1151  # From Horizon [C]
            elif in_[i] == 30:
                    # out(i)=0.17380000000000E+04; % From DITAN
                    # out(i)=1737.5;  % From Horizon [M1]
                out[i] = 1738.0   # From Horizon  [M3]
            elif in_[i] == 31:
                out[i] = 1367     # From Wertz, SMAD
                    # out(i)=1367.6;  % From Horizon  [W3]
            elif in_[i] == 32:
                out[i] = 365.25   # From Horizon
            else:
                print(f"Warning: Constant identifier {in_[i]} is not defined!")
                out[i] = 0
            
        return out


