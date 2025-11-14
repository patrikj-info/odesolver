from .ode import ODE 
from .plotter import Plotter 
from .solver import Solver 

import numpy as np

class ODESolver:
    """
        Class for solving ODEs.
    """

    EULER = "euler"
    AUTO_DIFF = "auto"

    def solveODE(ode:ODE, method:str, initial_conditions:list, t0:float, t_final:float, h:float) -> np.ndarray:
        """
            Solve an ODE.

            Parameters
            -----------------
                ode : ODE
                method : str
                initial_conditions : list
                t0 : float
                t_final : float
                h : float

            Returns
            -----------------
                np.ndarray
        """
        match method:
            case ODESolver.EULER:
                return Solver.EulerSolver(ode=ode, y0=initial_conditions, t0=t0, t_final=t_final, h=h)
            case ODESolver.AUTO_DIFF:
                return []
            case _:
                raise Exception(f"Unknown solve method: {method}")

    def plotSolution(data:np.ndarray, **kwargs) -> None:
        """
            Plot the obtained ODE solution.

            Parameters
            ---------------
                data : np.ndarray

        """
        Plotter.plot(data=data, animated=kwargs.get("animated", False), phase_space=kwargs.get("phase_space", False), save=kwargs.get("save", False), filename=kwargs.get("filename", ""), xlabel=kwargs.get("xlabel", ""), ylabel=kwargs.get("ylabel", ""), title=kwargs.get("title", ""), fps=kwargs.get("fps", 60), fileformat=kwargs.get("fileformat", ""))
        