import numpy as np
import numba
import matplotlib.pyplot as plt


class OdeSolver:
    """ 
    Class to solve ordinary differential equations using various numerical methods.
    Currently implemented methods:
    1. 4th Order Runge-Kutta
    """

    def __init__(self, rhs):
        """ 
        :param rhs:
        """
        self.rhs = rhs

    @numba.jit(nopython=True)
    def rk4_solve():
        return
