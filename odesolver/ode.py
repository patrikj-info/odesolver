import numpy as np
from itertools import groupby

def runs_after_x(s):
    results = []
    i = 0
    
    while i < len(s):
        if s[i] == 'x':
            count = 0
            j = i + 1
            while j < len(s) and s[j] == "'":
                count += 1
                j += 1
            results.append(count)
            i = j
        else:
            i += 1
    
    return results

class ODE:
    """
        Basic class for handling ODEs.
    """

    def __init__(self, order:int, funct:callable):
        """
            Initialize the ODE.

            Parameters
            ---------------
                order : int
                funct : callable
        """

        self.order = order 
        self.funct = funct 

    
    def __repr__(self):
        return "ODE()"
    
    def __str__(self):
        return f"ODE of order {self.order}"
    
    def get_order(self) -> int:
        return self.order
    
    def get_scalar_funct(self) -> callable:
        return self.funct

    def get_vect_funct(self) -> callable:
        def func(t, x):
            res = np.empty_like(x)
            res[:-1] = x[1:]
            res[-1] = self.funct(t,x)
            return res
        return func

    @staticmethod
    def readHomogenousODE(ode: str) -> "ODE":
        """
            Turns a given string into an ODE class. The input is always assumed to describe a homogenous ODE.
            The order should decrease from left to right.
            
            Example:

                ode = "2.0x'' - 3.0x' + 4.0x"

                not

                ode = "2.0x'' + 3.0x' + 4.0x = 0"

                This input then becomes:

                    x'' = (3.0x' - 4.0x)/2.0

            Parameters
            ----------------
                ode : str
            
            Returns
            ----------------
                ODE
        """

        # get the highest order present in the given ode (i.e. the highest consecutive amount of ')
        highest_order = max((len(list(group)) for char, group in groupby(ode) if char == "'"), default=0)
    
        # get all present orders, including 0
        all_orders = runs_after_x(ode)

        # prepare array for coefficients
        coeffs = np.zeros(shape=(highest_order + 1, 1))

        # only get coefficients
        s = ode.replace("+", "").replace(" ", "").replace("'", "").split("x")

        # iterate through all orders:
        # 1. is the order present in all_orders? -> get its non-zero coefficient
        # 2. is the order not present in all_orders? -> set its coeffient to zero 
        for i in range(highest_order + 1):
            if i not in all_orders:
                coeffs[i] = 0.0
            else:
                index = np.where(np.array(all_orders) == i)[0][0]
                coeffs[i] = float(s[index])

        # create the respective function for Eulers Method
        def make_func(coeffs):
            def func(t, x):
                return -sum(c * xi for c, xi in zip(coeffs[0:-1], x))/coeffs[-1]
            return func

        func =  make_func(coeffs)

        # return the ODE
        return ODE(order=highest_order, funct=func)               

    @staticmethod
    def readODE(ode: str, inhom:callable) -> "ODE":

        # get the highest order present in the given ode (i.e. the highest consecutive amount of ')
        highest_order = max((len(list(group)) for char, group in groupby(ode) if char == "'"), default=0)
    
        # get all present orders, including 0
        all_orders = runs_after_x(ode)

        # prepare array for coefficients
        coeffs = np.zeros(shape=(highest_order + 1, 1))

        # only get coefficients
        s = ode.replace("+", "").replace(" ", "").replace("'", "").split("x")

        # iterate through all orders:
        # 1. is the order present in all_orders? -> get its non-zero coefficient
        # 2. is the order not present in all_orders? -> set its coeffient to zero 
        for i in range(highest_order + 1):
            if i not in all_orders:
                coeffs[i] = 0.0
            else:
                index = np.where(np.array(all_orders) == i)[0][0]
                coeffs[i] = float(s[index])

        # create the respective function for Eulers Method
        def make_func(coeffs):
            def func(t, x):
                return inhom(t,x)/coeffs[-1] - sum(c * xi for c, xi in zip(coeffs[0:-1], x))/coeffs[-1]
            return func

        func = make_func(coeffs)

        # return the ODE
        return ODE(order=highest_order, funct=func)               
