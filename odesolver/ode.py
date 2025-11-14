import numpy as np

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
    
    def get_funct(self) -> callable:
        return self.funct