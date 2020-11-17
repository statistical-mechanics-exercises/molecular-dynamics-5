# Visualising your results

We now really have everything we need in order to generate molecular dynamics trajectories as:

1. We know how to calculate the forces for a given configuration.
2. We know how to code the Verlet algorithm and to thus work out how the positions and the velocities of the atoms change with time.
3. We know how to compute the instantaneous values of the potential and kinetic energy.  We can use these values to check if we are using a sufficiently small value for the timestep as, if the timestep is too large, energy will not be conserved during our simulation.

Your task in this final exercise is thus to write one final MD code that incorporates all these elements.  In doing so you will need to:

1. Write a function called `potential` that computes the potential energy and the forces for each of the configurations you generate.
2. Write a function called `kinetic` that calculates the instantaneous kinetic energy.
3. Use your potential function to write code that uses the velocity Verlet algorithm to integrate the equations of motion.
4. Every 10 MD steps store the instantaneous values of the potential, kinetic and total energies in the lists called `p_energy`, `k_energy` and `t_energy`

I have written a skeleton code in `main.py` to get you started.  If this code is completed correctly a graph should be generated that shows how the potential, kinetic and total energy change as the simulation progresses. 
