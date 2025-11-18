import numpy as np
from ode import ODE

class Solver:
    """
        Class for solving ODEs numerically.
    """

    RK4_CONSTANTS = [1/6, 1/3, 1/3, 1/6]

    def EulerSolver(ode:ODE, y0:np.ndarray, t0:float, t_final:float, h:float) -> np.ndarray:
        """
            This solves the given n-dimensional ODE numerically using Euler's method.

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
        ode_dim = ode.get_dimension()
        
        # Initialize storage for results
        results = np.empty((ode_order + 1, steps + 1, ode_dim))

        # Initial conditions
        y = y0.copy()
        t_i = t0

        # Temporary storage
        y = np.array(y, dtype=float)
        y = y.reshape((2,ode_dim))

        temp_y = np.zeros_like(y)
        tx = np.zeros(shape=(1, ode_dim), dtype=float) + t0

        # Add initial conditions
        results[0,0] = tx
        results[1:,0]= y

        # Euler Method
        for i in range(steps):
            # advance time
            t_old = t_i
            t_i += h

            # reset temp values
            temp_y[:] = 0

            # update
            for n in range(ode_order - 1):
                temp_y[n] = y[n] + h * y[n + 1]

            f_val = ode_funct(t_old, y)

            temp_y[-1] = y[-1] + h * f_val

            # copy values
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

    def unpackData(data:np.ndarray, axis:tuple[int] = (0, 1, 2)) -> tuple[np.ndarray]:        
        """
            Unpack the data received from the numerically solvers.

            Parameters
            -------------------
                data : np.ndarray
                    The raw data.
                axis : tuple
                    The axes, which are to be used for unpacking. For example, time is indexed with 0, while the variable is 1 and its first derivative 2 etc.

            Returns
            -------------------
                tuple[np.ndarray]
                    The unpacked data.
        """

        if len(axis) == 0:
            raise Exception("No axis given!")

        return_tuple = []

        for i in range(len(axis)):
            if i == 0:
                t = np.unique(data[0])
                return_tuple.append(t)
            else:
                index = axis[i]
                return_tuple.append(data[index])

        return tuple(return_tuple)