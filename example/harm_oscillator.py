from odesolver.ode import ODE
from odesolver.odesolver import ODESolver
from odesolver.plotter import Plotter
from odesolver.solver import unpackData

# load ode
ode = ODE.readHomogenousODE("4.0x'' + 0.1x' + 2.0x")

# find solution using Euler's method
sol = ODESolver.solveODE(ode=ode, method="euler", initial_conditions=[1.0, 0.0], t0=0, t_final=10, h=0.01)

# unpack data 
t, x = unpackData(sol, (0,1))

# plot solution
Plotter.plot(t,x, filename="harm_oscillator_euler.png", fileformat="png")

# find solution using Runge-Kutta 4
sol = ODESolver.solveODE(ode=ode, method="rk4", initial_conditions=[1.0, 0.0], t0=0, t_final=10, h=0.01)

# plot solution
Plotter.plot(t,x, filename="harm_oscillator_rk4.png", fileformat="png")