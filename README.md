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

# Disclaimer
```diff
- This code has been developed for personal research purposes and it should not be used for replacing anything.
- The author is not responsible for errors or bugs in the code. 
```




