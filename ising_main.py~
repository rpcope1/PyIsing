#!/usr/bin/python
#Ising Model Simulation
#Robert Cope 2013

from ising_grid import *
#from ising_gui import *
from ising_gui import ising_gui
import time
import pylab

def set_values(igrid, disp, x_dim, y_dim):
    up = (0, 0, 0x00)
    down = (0, 0,0xFF)
    retv = (igrid.get_T(), igrid.get_E_total(), igrid.get_G_avg())
    disp.set_temperature(retv[0])
    disp.set_energy(retv[1])
    disp.set_correlation(retv[2])

    for j in range(y_dim):
            for i in range(x_dim):
                value = igrid.get_val(i, j)
                if(value == 1):
                    disp.set_pixel(i, j, (0, 0, 0x00))
                elif(value == -1):
                    disp.set_pixel(i, j, (0, 0, 0xFF))
                else:
                    disp.set_pixel(i, j, (0x00, 0xFF, 0xFF))

    return retv

if __name__ == "__main__":
    x_dim = 40
    y_dim = 40
    grid = ising_grid(x_dim, y_dim)
    disp = ising_gui(x_dim, y_dim)    

    listT = []
    listE = []
    listG = []
    
    T_start = 3.0
    T_end = 1.0
    T = T_start
    grid.set_T(T_start)
    grid.set_B(0.00)
    grid.set_J(1.00)
    
    itr = 0
    itr_max = 250
    grid.randomize()
    #We're going to run a simulated annealing.
    while(itr < itr_max):
        (T, E, G) = set_values(grid, disp, x_dim, y_dim)
        disp.draw()
        monte_carlo_update(grid)
        print "Temp = ", T, "Total Energy = ", E, "Order parameter = ", G
        listE.append(E)
        listT.append(T)
        listG.append(G)
        T = T_start - (itr/(1.0*itr_max))*(T_start-T_end)
        grid.set_T(T)        
        itr += 1
        time.sleep(0.05)

    pylab.plot(listT, listG, "r+")
    pylab.xlabel("Temperature")
    pylab.ylabel("Order Parameter G")
    pylab.show()
