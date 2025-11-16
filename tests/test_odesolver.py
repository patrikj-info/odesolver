import pytest 
from odesolver.ode import ODE 
from odesolver.odesolver import ODESolver
from odesolver.plotter import Plotter

import numpy as np

def test():
    ode = ODE.readHomogenousODE("2.0x'' + 0.1x' + 3.0x")
    res1 = ODESolver.solveODE(ode=ode, method=ODESolver.RUNGE_KUTTA_4, initial_conditions=[1.0, 0.0], t0=0, t_final=100, h=0.0001)
    res2 = ODESolver.solveODE(ode=ode, method=ODESolver.EULER, initial_conditions=[1.0, 0.0], t0=0, t_final=100, h=0.0001)
    ODESolver.plotSolution(res1, save=True, fileformat=Plotter.PNG_FORMAT, animated=False, fps=300, filename="test_rk4.png")
    ODESolver.plotSolution(res2, save=True, fileformat=Plotter.PNG_FORMAT, animated=False, fps=300, filename="test_euler.png")


if __name__ == "__main__":
    test()
