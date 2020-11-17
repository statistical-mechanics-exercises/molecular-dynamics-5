import matplotlib.pyplot as plt
import numpy as np

def potential(x) :
  energy = 0 
  forces = np.zeros([7,2])
  # Your code to calculate the potential goes here
  
  return energy, forces
  
def kinetic(v) :
  ke = 0
  # Your code to calculate the kinetic energy from the velocities goes here
  
  return ke
  
# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This command reads in the velocities that are contained in the file called velocities.txt
vel = np.loadtxt( "velocities.txt" )

# This is the value to use for the timestep (the delta in the equations on the other side)
timestep = 0.005
# This calculates the initial values for the forces
eng, forces = potential(pos)

# We now run 500 steps of molecular dynamics
nsteps = 500
times = np.zeros(int(nsteps/10))
k_energy = np.zeros(int(nsteps/10))
p_energy = np.zeros(int(nsteps/10))
t_energy = np.zeros(int(nsteps/10))
for step in range(nsteps) :
  # First update the velocities a half timestep
  # fill in the blanks in the code here
  for i in range(7) : 
    vel[i][0] = 
    vel[i][1] = 
    
  # Now update the positions using the new velocities
  # You need to add code here
  
  
  # Recalculate the forces at the new position
  # You need to add code here
  eng, forces = 
  
  # And update the velocities another half timestep
  # You need to add code here


  # This is where we want to store the energies and times
  if step%10==0 : 
    times[int(step/10)] = step
    p_energy[int(step/10)] = eng 
    # Write code to ensure the proper values are saved here
    k_energy[int(step/10)] =
    t_energy[int(step/10)] =
  
 
# This will plot the potential, kinetic and total energy as a function of 
# time
plt.plot( times, p_energy, 'b-' )
plt.plot( times, k_energy, 'r-' )
plt.plot( times, t_energy, 'k-' )
plt.savefig( "energies.png" )
