import math
from math import exp
import random

random.seed()



def set_mode(igrid, F):
    return (exp(2*(igrid.J*F + igrid.B)*igrid.Beta), exp(-2*(igrid.J*F + igrid.B)*igrid.Beta))

def monte_carlo_update(igrid):
    y_max = igrid.y_max
    x_max = igrid.x_max
    modes = {}
    for i in [0, 2, 4, -2, -4]: #Build look up table instead of evaluating exponential to save time.
        modes[i] = set_mode(igrid, i)
    for j in range(y_max):
        for i in range(x_max):
            val = igrid.get_val(i,j)
            if(val == -1):
                r = modes[igrid.get_F(i, j)][0]
            elif(val == 1):
                r = modes[igrid.get_F(i, j)][1]
            if(r > 1):
                igrid.flip(i, j)
            else:
                if(r > random.random()):
                    igrid.flip(i, j)


class ising_grid(object):    
    def __init__(self, x_dim=10, y_dim=10, copy=None):
            if(copy is not None):
                self.x_max = len(copy[0])
                self.y_max = len(copy)
                self.grid = []
                cgrid = copy.get_grid()
                for j in range(self.y_max):
                         self.grid.append(cgrid[j][:])                       
                self.J = copy.get_J()
                self.B = copy.get_B()
                self.T = copy.get_T()
                self.Beta = 1/self.T
                self.hamiltonian = copy.get_Hamiltonian()
            else:
                self.grid = []
                self.x_max = x_dim
                self.y_max = y_dim
                for j in range(y_dim):
                    self.grid.append([0 for i in range(x_dim)])
                self.J = 1.0
                self.B = 1.0
                self.T = 1.0
                self.Beta = 1/self.T   

    def randomize(self):
        for j in range(self.y_max):
            for i in range(self.x_max):
                self.grid[j][i] = random.choice([-1,1]) #It can either take on a value of 1 or 0.
         

    def ising_hamiltonian(self, i, j):
        Y_MAX = self.y_max
        X_MAX = self.x_max
        return -self.grid[j%Y_MAX][i%X_MAX]*(self.J*(self.grid[(j-1)%Y_MAX][i%X_MAX] + self.grid[(j+1)%Y_MAX][i%X_MAX] + self.grid[j%Y_MAX][(i+1)%X_MAX] + self.grid[j%Y_MAX][(i-1)%X_MAX]) + self.B)

    def set_J(self, J):
        self.J = J

    def set_B(self, B):
        self.B = B

    def set_T(self,T):
        self.T = T
        self.Beta = 1/float(T)

    def set_Beta(self, Beta):
        self.Beta = Beta
        self.T = 1.0/float(Beta)

    def get_T(self):
        return self.T

    def get_Beta(self):
        return self.Beta

    def get_J(self):
        return self.J
    
    def get_B(self):
        return self.B
    
    def get_E_total(self):
        E_total = 0.0
        for j in range(self.y_max):
            for i in range(self.x_max):
                E_total += self.eval_H(i, j)
        return E_total
        
    def get_Hamiltonian(self):
        return self.hamiltonian

    def eval_H(self, i, j):
        return self.ising_hamiltonian(i, j)

    def get_val(self, i, j):
        return self.grid[j][i]    

    def set_val(self, value, i, j):
        self.grid[j][i] = value

    def flip(self, i, j):
        self.grid[j][i] *= -1

    def get_F(self, i, j):
        X_MAX = self.x_max
        Y_MAX = self.y_max
        return (self.grid[(j-1)%Y_MAX][i%X_MAX] + self.grid[(j+1)%Y_MAX][i%X_MAX] + self.grid[j%Y_MAX][(i+1)%X_MAX] + self.grid[j%Y_MAX][(i-1)%X_MAX])

    def get_G(self, i, j):
        return self.get_F(i, j)*self.get_val(i,j)/4.0

    def get_G_avg(self):
        total = 0.0
        for j in range(self.y_max):
            for i in range(self.x_max):
                total += self.get_G(i, j)
        total /= (1.0*self.x_max*self.y_max)
        return total

    def get_grid(self):
        return self.grid

    def copy_grid(self, cgrid):
        for j in range(self.y_max):
            self.grid[j] = cgrid[j][:]
