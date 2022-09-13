# imports
import numpy as np
import scipy


class RootFinder:

    """
    Find roots of a function using numerical methods
    """

    def __init__(self, func):
        """
        :param func:           function of one variable for which to find roots
        """
        self.func = func

    def _bisection_method(self, xmin, xmax, accuracy, print_efficiency=False):
        """
        Find roots of self.func using bisection method

        :param xmin:                minimum x value in desired range
        :param xmax:                maximum x value in desired range
        :param accuracy:            magnitude (close to 0) of function at which to define a root (e.g 10^-4) 
        :param print_efficiency:    ouput number of function evals if True. 
        """

        # rewrite variable names:
        x1 = xmin
        x2 = xmax

        # initialize values
        root = 1/2*(x1+x2)
        f1 = self.func(x1)
        f2 = self.func(x2)
        f3 = self.func(root)

        # return if no root:
        if np.sign(f1) == np.sign(f2):
            print("Bracket Error: f(xmin) has same sign as f(xmax)")
            return None

        # limit number of iterations as a safety
        max_iterations = 10**3
        i = 0

        while (abs(f3) > accuracy) and (i < max_iterations):
            if np.sign(f3) == np.sign(f1):
                x1, f1 = root, f3
            elif np.sign(f3) == np.sign(f2):
                x2, f2 = root, f3
            else:
                # if it has neither of their signs then it must be 0
                return root

            root = 1/2*(x1+x2)
            f3 = self.func(root)
            i += 1

        # output efficiency (assuming did not pass the max iterations)
        if print_efficiency:
            # 3 extra function evals to initialize loop
            print("Number of function calls: ", i + 3)

        # if we passed the max_iterations then we assume there is a bug and return None
        return root if i < max_iterations else None

    def _false_position_method(self, xmin, xmax, accuracy, print_efficiency=False):
        """
        Find roots of self.func using false position method

        :param xmin:                minimum x value in desired range
        :param xmax:                maximum x value in desired range
        :param accuracy:            magnitude (close to 0) of function at which to define a root (e.g 10^-4) 
        :param print_efficiency:    ouput number of function evals if True. 
        """

        # rename variables:
        x1 = xmin
        x2 = xmax

        # initialize function vals
        f1 = self.func(x1)
        f2 = self.func(x2)
        root = x1 - f1*((x2-x1)/(f2-f1))
        f3 = self.func(root)

        # return if no root:
        if np.sign(f1) == np.sign(f2):
            print("Bracket Error: f(xmin) has same sign as f(xmax)")
            return None

        # limit number of iterations as a safety
        max_iterations = 10**3
        i = 0

        while (abs(f3) > accuracy) and (i < max_iterations):

            if np.sign(f3) == np.sign(f1):
                x1, f1 = root, f3
            elif np.sign(f3) == np.sign(f2):
                x2, f2 = root, f3
            else:
                # if it has neither of their signs then it must be 0
                return root
            i += 1

            root = x1 - f1*((x2-x1)/(f2-f1))
            f3 = self.func(root)

        # output efficiency (assuming did not pass the max iterations)
        if print_efficiency:
            # 3 extra function evals to initialize loop
            print("Number of function calls: ", i + 3)

        # if we passed the max_iterations then we assume there is a bug and return None
        return root if i < max_iterations else None
