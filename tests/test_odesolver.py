import pytest 
from odesolver.ode import ODE 
from odesolver.odesolver import ODESolver

def test():
    ode = ODE.readHomogenousODE("5.0x'' + 1.0x' + 3.0x")
    res = ODESolver.solveODE(ode=ode, method=ODESolver.EULER, initial_conditions=[1.0, 0.0], t0=0, t_final=50, h=0.01)
    ODESolver.plotSolution(res)

if __name__ == "__main__":
    pytest.main()
