
import unittest
import numpy as np
from zzoopt import ZooptOptimizer
from scipy.optimize import OptimizeResult

def ackley(x):
    """
    Ackley function for continuous optimization
    """
    bias = 0.2
    ave_seq = sum([(i - bias) * (i - bias) for i in x]) / len(x)
    ave_cos = sum([np.cos(2.0 * np.pi * (i - bias)) for i in x]) / len(x)
    value = -20 * np.exp(-0.2 * np.sqrt(ave_seq)) - np.exp(ave_cos) + 20.0 + np.e
    return value

def rosen(x):
     """The Rosenbrock function"""
     x = np.array(x)
     return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

class TestZoopt(unittest.TestCase):

    def setUp(self):
        self.optimizer= ZooptOptimizer(options={"budget_per_dim": 1000})

    def test_optimization(self):
        results = self.optimizer.minimize(ackley, initial_params=[10.0, 10.0])
        print(results)
        results = self.optimizer.minimize(rosen, initial_params=[0.0, 0.0])
        print(results)
        # PENDING
        # self.assertAlmostEqual(results.opt_value, 0, places=5)
        # self.assertAlmostEqual(results.opt_params[0], 1, places=4)
        # self.assertAlmostEqual(results.opt_params[1], 1, places=4)
        # self.assertIn("nfev", results.keys())
        # self.assertIn("nit", results.keys())
        # self.assertIn("opt_value", results.keys())
        # self.assertIn("opt_params", results.keys())
        # self.assertIn("history", results.keys())