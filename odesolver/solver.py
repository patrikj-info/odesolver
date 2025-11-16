import numpy as np
from .ode import ODE

class Solver:
    """
        Class for solving ODEs numerically.
    """

    RK4_CONSTANTS = [1/6, 1/3, 1/3, 1/6]
    
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
        ode_funct = ode.get_scalar_funct()

        # Initialize storage for results
        results = np.empty((ode_order + 1, steps + 1))

        # Initial conditions
        y = y0.copy()
        t_i = t0

        # Temporary storage
        temp_y = np.empty_like(y)

        # Add initial conditions
        results[0,0] = t0 
        results[1:,0] = y

        # Euler Method
        for i in range(steps):
            # advance time
            t_old = t_i
            t_i += h

            # update
            for n in range(ode_order - 1):
                temp_y[n] = y[n] + h * y[n + 1]

            temp_y[-1] = y[-1] + h * ode_funct(t_old, y)

            y = temp_y.copy()

            # save time and solution
            results[0, i+1] = t_i
            results[1:, i+1] = y

        return results

    def RungeKutta4Solver(ode:ODE, y0:np.ndarray, t0:float, t_final:float, h:float) -> np.ndarray:
        """
            This solves the given ODE numerically using the Runge-Kutta method of order 4.

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
        ode_funct = ode.get_vect_funct()

        # Initialize storage for results
        results = np.empty((ode_order + 1, steps + 1))

        # Initial conditions
        y = y0.copy()
        t_i = t0

        # Add initial conditions
        results[0,0] = t0
        results[1:, 0] = y 

        y = np.array(y)

        # RK4 Method
        for i in range(steps):
            # advance time
            t_older = t_i
            t_i += h
            # update
            # for n in range(ode_order):
            #     temp_y[n] = y[n]

            k_1 = ode_funct(t_older, y)
            k_2 = ode_funct(t_older + h/2, y + h/2*k_1)
            k_3 = ode_funct(t_older + h/2, y + h/2*k_2)
            k_4 = ode_funct(t_older + h, y + h*k_3)
            k = [k_1, k_2, k_3, k_4]
                # print(f"{k=}")

            for j in range(4):
                k_n = Solver.RK4_CONSTANTS[j]*k[j]                     
                y += h * k_n

            # y = temp_y.copy()

            # save time and solution
            results[0, i+1] = t_i
            results[1:, i+1] = y

        return results

    def AutoSolver(ode:ODE, y0:np.ndarray, t0:float, t_final:float) -> np.ndarray:
        return np.zeros(shape=(1,1))
