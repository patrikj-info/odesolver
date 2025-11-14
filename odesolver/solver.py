import numpy as np
from ode import ODE

class Solver:
    """
        Class for solving ODEs numerically.
    """

    def EulerSolver(ode:ODE, y0:np.ndarray, t0:float, t_final:float, h:float) -> np.ndarray:
        """
            This solves the given ODE numerically using Euler's method.

            Parameters
            ----------------
                ode : ODE
                    The ODE to be solved.
                y0 : np.ndarray
                    Initial conditions.
                t0 : float
                    Starting time.
                t_final : float
                    Final time.
                h : float
                    Step size.

            Returns
            -----------------
                np.ndarray
                    Numeric solution.
        """
        
        # Get number of required steps
        steps = int((t_final - t0) / h)

        # Get ODE properties
        ode_order = ode.get_order()
        ode_funct = ode.get_funct()

        # Initialize storage for results
        results = np.empty((ode_order + 1, steps))

        # Initial conditions
        y = y0.copy()
        t_i = t0

        # Temporary storage
        temp_y = np.empty_like(y)

        # Add initial conditions
        results[0][0] = t0 
        for i in range(len(y)):
            results[i + 1][0] = y[i]

        # Euler Method
        for i in range(steps):
            # advance time
            t_i += h

            # update
            for n in range(ode_order - 1):
                temp_y[n] = y[n] + h * y[n + 1]

            temp_y[-1] = y[-1] + h * ode_funct(t_i, y)

            y = temp_y.copy()

            # save time and solution
            results[0][i] = t_i

            for j in range(len(y)):
                results[j + 1][i] = y[j]

        return results


        