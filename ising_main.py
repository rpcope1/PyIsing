#!/usr/bin/python
#Ising Model Simulation
#Robert Cope 2013

from ising_grid import *
#from ising_gui import *
from wall import Wall
import time
import pylab

def set_values(igrid, wall, x_dim, y_dim):
    up = (0, 0, 0x00)
    down = (0, 0,0xFF)
    for j in range(y_dim):
            for i in range(x_dim):
                value = igrid.get_val(i, j)
                if(value == 1):
                    wall.set_pixel(i, j, (0, 0, 0x00))
                elif(value == -1):
                    wall.set_pixel(i, j, (0, 0, 0xFF))
                else:
                    wall.set_pixel(i, j, (0x00, 0xFF, 0xFF))


if __name__ == "__main__":
    x_dim = 40
    y_dim = 40
    grid = ising_grid(x_dim, y_dim)
    T_start = 7.6
    T_end = 0.01
    grid.set_T(T_start)
    grid.set_B(0.00)
    grid.set_J(1.00)
    disp = Wall(x_dim, y_dim)
    itr = 0
    itr_max = 250
    grid.randomize()
    listT = []
    listE = []
    listG = []
    while(itr < itr_max):
        set_values(grid, disp, x_dim, y_dim)
        disp.draw()
        monte_carlo_update(grid)
        T = T_start - (itr/(1.0*itr_max))*(T_start-T_end)
        grid.set_T(T)
        E = grid.get_E_total()
        G = grid.get_G_avg()        
        print "Temp = ", T, "Total Energy = ", E, "Order parameter = ", G
        listE.append(E)
        listT.append(T)
        listG.append(G)        
        itr += 1
        time.sleep(0.05)

    pylab.plot(listT, listG, "r+")
    pylab.xlabel("Temperature")
    pylab.ylabel("Order Parameter G")
    pylab.show()
