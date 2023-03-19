# Orbital-Mechanics-Exercises

Simple Python codes solving exercises from the Politecnico di Milano's course Orbital Mechanics. In this repository you can find 6 exercises, divided in 2 laboratories, covering the following problems:
- Orbit integration in the Unperturbed 2 Body Problem (U2BP) and computation of the variation of the orbit's parameters. 
- Orbit integration in the Perturbed 2 Body Problem under J2 (J22BP) and computation of the variation of the orbit's parameters. 
- Solver for Kepler’s equation.
- Computation of ground track under the U2BP and the J22BP.

# Prerequisites
You will need to have Python installed on your machine.

# Installing
Clone the repository to your local machine using git clone:
bash
Copy code
git clone https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises.git

# Acknowledgements
This code was developed by me as part of a project in Orbital Mechanics at Politecnico di Milano. 

# Laboratory N.1
## Exercise 1: Orbit Propagation in the unperturbed 2 body problem

This is a Python script for propagating an orbit using its initial state in Cartesian coordinates. It uses the equations of motion of an orbit reduced to a first order ODE system and propagates them through a function called "tbp_ode".

Usage: To use the script, run the Es1.py file in your Python environment. The script will plot the orbit of the Earth and the variation of the energy, angular momentum, eccentricity, true anomaly, radial and tangential velocities of the same orbit.

Example plot: 

<p align="center">
  <img src="https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises/blob/main/Lab1/Es1/Es1.png" />
</p>
<p align="center">
  <em>Figure 1. Results of the exercise 1.</em>
</p>

## Exercise 2: Orbit Propagation in the perturbed 2 body problem under J2

This is a Python script for propagating an orbit using its initial state in Cartesian coordinates under the perturbation of the Earth's oblateness (J2). It uses the equations of motion of an orbit reduced to a first order ODE system and propagates them through a function called "tbp_ode2".

Usage: To use the script, run the Ex2.py file in your Python environment. The script will plot the orbit of the Earth and the variation of the energy, angular momentum, eccentricity, true anomaly, radial and tangential velocities of the same orbit.

Example plot: 

<p align="center">
  <img src="https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises/blob/main/Lab1/Es2/Es2.png" />
</p>
<p align="center">
  <em>Figure 2. Results of exercise 2.</em>
</p>

## Exercise 3: Kepler's Equation Solver

This is a Python script for solving Kepler's equation, given the eccentricity, the semi-major axis, the time vector and other constants. The script uses the Newton-Raphson method to solve the equation iteratively, until the required accuracy is achieved. The function is called "kepler_solver".

Usage: To use the script, run the Ex3.py file in your Python environment calling the "kepler_solver" function and pass the required inputs. The function will return the true anomaly of the orbit for each time instant and the script will plot a surface like this: 

<p align="center">
  <img src="https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises/blob/main/Lab1/Es3/Es3.png" />
</p>
<p align="center">
  <em>Figure 3. Results of exercise 3.</em>
</p>

# Laboratory N. 2

## Exercise 1: Ground Track Computation

This is a Python script for computing the ground track of an orbit, given its state at the initial time (either in Cartesian or Keplerian elements).

Usage: To use the script, run the Ex1.py file in your Python environment, calling the "ground_track" function and pass the required inputs. The function will return the longitude and latitude of the projection of the orbit on the Earth (ground track).

Example plot: 
<p align="center">
  <img src="https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises/blob/main/Lab2/Es1/Es1.png" />
</p>
<p align="center">
  <em>Figure 4. Results of exercise 1.</em>
</p>

## Exercise 2: Repeating Ground Track
This is a Python script for computing the required semi-major axis for a repeating ground track orbit, given the number of satellite revolutions and the number of Earth revolutions. The function used is called "repeating_ground_track".

Usage: To use the script, run the Ex2.py file, calling call the "repeating_ground_track" function and pass the required inputs. The function will return the required semi-major axis for the given parameters.

Example plot: 
<p align="center">
  <img src="https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises/blob/main/Lab2/Es2/Es2.png" />
</p>
<p align="center">
  <em>Figure 5. Results of exercise 2.</em>
</p>

## Exercise 3: Repeating Ground Track with J2 Perturbations
This exercise builds upon Exercise 5, but takes into account the J2 perturbations on the orbit propagation and the computation of the required semi-major axis for a repeating ground track.

To incorporate J2 perturbations into the orbit propagation, I substituted the "tbp_ode" function with the "tbp_ode2" function of exercise 2, laboratory 1.

To compute the required semi-major axis for a repeating ground track with J2 perturbations, I modified the RepeatingGroundTrack function from Exercise 5. The modified function is called RepeatingGroundTrackPerturbed and takes into account the J2 perturbations in the computation of the longitude of the ascending node and the argument of perigee.

Usage: To use the modified function, run the Ex3.py file in your Python environment. The script will compute the required semi-major axis for a repeating ground track with J2 perturbations and plot the resulting ground track.

Example plot:

<p align="center">
  <img src="https://github.com/giovannifacchinetti99/Orbital-Mechanics-Exercises/blob/main/Lab2/Ex6/Ex6.png" />
</p>
<p align="center">
  <em>Figure 6. Results of exercise 3.</em>
</p>

# Disclaimer
```diff
- This code has been developed for personal research purposes and it should not be used for replacing anything.
- The author is not responsible for errors or bugs in the code. 
```




