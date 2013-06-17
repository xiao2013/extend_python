import sys
import pylab as pl
import rk4
import numpy as np
#	Runge Kutta for set of first order differential equations

# 	PROGRAM oscillator
#   	IMPLICIT none
#
# 		declarations
# N:number of equations, nsteps:number of steps, tstep:length of steps

# 		y(1): initial position, y(2):initial velocity
y=np.zeros(2,'d')	
N=2
nsteps=300
tstep=0.1
t=0.0
y[0]=1.0
y[1]=0.0
x = np.zeros(1,'d')
tim = np.zeros(1,'d')
x[0] = y[0]
tim[0] = t
# 	do loop n steps of Runga-Kutta algorithm
for j in range(0,nsteps):
	t=j*tstep
   	rk4.rk4(t, tstep, y, N)
	x = np.append(x, y[0])
	tim = np.append(tim, t)

print t
print tim
pl.plot(tim,x)
