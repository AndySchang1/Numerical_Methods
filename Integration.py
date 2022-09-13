
import numpy as np


class Integrator:

    """
    Integrator class to integrate one dimensional functions using various numerical 
    integration techniques.
    Currently implemented techniques:
    1. Trapezoid Rule
    """

    def __init__(self, func):
        """
        :param func:     A function of one variable (f(x)) for which to integrate over.
        """

        self.func = func

    def _trapezoid(self, x0, x1, n_max, n_min=8, threshold=0.00001):
        """
        Efficiently integrates self.func from x0 to x1 with increasing numbers of steps using trapezoid rule by using values calculated in each previous step

        :param x0:          Lower bound of integral
        :param x1:          Upper bound of integral
        :param n_max:       Maximum number of points evaluated in integral (unless threshold achieved)
        :param n_min        Minimum number of points to be evaluated before terminating loop
        :param thresh:      Threshold of accuracy at which to stop integrating
        """

        # initialize sum
        sum = 0.5*(self.func(x0) + self.func(x1))

        # initialize list of integral values
        i_new = sum*(x1-x0)
        i_old = np.inf

        # store integral values we initialize the return list
        res = []
        # loop until either threshold or n_max is reached (here n is actually half the number of points in use)
        n = 1
        while((2*n <= n_max and abs(i_new - i_old) > threshold) or 2*n < n_min):
            n *= 2
            h = (x1-x0)/n
            temp = 0
            i_old = i_new
            res.append(i_new)
            # calculate function value at odd steps
            for j in range(1, n, 2):
                temp += self.func(x0 + j*h)

            sum += temp
            i_new = sum*h

        # return integral values for all n
        return res
