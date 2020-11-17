import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_kinetic(self) :
        for i in range(10) :
            vel = np.zeros([7,2])
            myeng = 0
            for j in range(7) : 
                vel[j,0], vel[j,1] = np.random.normal(), np.random.normal()
                myeng = myeng + vel[j,0]*vel[j,0] / 2 + vel[j,1]*vel[j,1] / 2
            self.assertTrue( np.abs( kinetic(vel) - myeng )<1e-6, "The kinetic energy is not computed correctly" )
            
    def test_forces(self) :
        pp = pos
        # Get the positions and analytic forces
        base_p, base_f = potential(pp)
        for i in range(7) :
           for j in range(2) :
              pp[i][j] = pp[i][j] + 1E-8
              new_p, crap = potential(pp)
              numder = (new_p-base_p)/1E-8
              self.assertTrue( np.abs(numder + base_f[i][j])<1e-4, "Forces and potential are not consistent" )
              pp[i][j] = pp[i][j] - 1E-8
              
    def test_trajectory(self) :
        mypos = np.loadtxt("positions.txt")
        myvel = np.loadtxt("velocities.txt")
        eng, myforces = potential(mypos)
 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        times, this_pe = zip(*figdat)
        figdat = fighand.get_lines()[1].get_xydata()
        times, this_ke = zip(*figdat)
        figdat = fighand.get_lines()[2].get_xydata()
        times, this_te = zip(*figdat)

        for step in range(nsteps) :
            for i in range(7) : 
                myvel[i][0] = myvel[i][0] + 0.5*timestep*myforces[i][0]
                myvel[i][1] = myvel[i][1] + 0.5*timestep*myforces[i][1]

            for i in range(7) : 
                mypos[i][0] = mypos[i][0] + timestep*myvel[i][0]
                mypos[i][1] = mypos[i][1] + timestep*myvel[i][1]
  
            eng, myforces = potential(mypos)
  
            for i in range(7) : 
                myvel[i][0] = myvel[i][0] + 0.5*timestep*myforces[i][0]
                myvel[i][1] = myvel[i][1] + 0.5*timestep*myforces[i][1]
 
            if step%10==0 : 
               self.assertTrue( np.abs( eng - this_pe[int(step/10)] )<1E-4, "The trajectory is incorrect" )
               kes = kinetic(myvel)
               self.assertTrue( np.abs( kes - this_ke[int(step/10)] )<1E-4, "The trajectory is incorrect" )
               self.assertTrue( np.abs( kes + eng - this_te[int(step/10)] )<1E-4, "The trajectory is incorrect" )
  
   
