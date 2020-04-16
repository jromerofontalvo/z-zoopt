from zquantum.core.interfaces.optimizer import Optimizer
from scipy.optimize import OptimizeResult
from zoopt import Dimension, ValueType, Dimension2, Objective, Parameter, Opt, Solution
import numpy as np

import copy

class ZooptOptimizer(Optimizer):

    def __init__(self, options=None):
        """
        list of options:
        dim_size (Number of dimensions)
        boundaries (tuple)
        """
        if options is None:
            options = {}
        if "boundaries" not in options.keys():
            options["boundaries"] = [-2.0 * np.pi, 2.0 * np.pi]
        if "budget_per_dim" not in options.keys():
            options["budget_per_dim"] = 100
        if "exploration_rate" not in options.keys():
            options["exploration_rate"] = 0.01
        if "seed" not in options.keys():
            options["seed"] = None
        self.options = options

    def minimize(self, cost_function, initial_params):
        """Minimize using the Zoopt optimizer in high-dimensional mode

        Args:
            cost_function: the function whose return value is to be minimized.
            initial_params (numpy.ndarray): initial guess for the ansatz parameters.
        Returns:
            tuple: A tuple containing an optimization results dict and a numpy array
                with the optimized parameters.
        """

        # Optimization Results Object
        history = []
        dim_size = len(initial_params)
        def wrapped_cost_function(params):
            params_x = params.get_x()
            value = cost_function(params_x)
            history.append({'params': params_x, 'value': value})
            print(f'Function evaluation {len(history)}: {value}', flush=True)
            print(f'{params}', flush=True)
            return value

        # define dimensions
        dim = Dimension(dim_size, [self.options["boundaries"]] * dim_size, [True] * dim_size)
        # define objective
        objective = Objective(wrapped_cost_function, dim)
        # define parameters
        budget = self.options["budget_per_dim"] * dim_size
        parameter = Parameter(budget=budget, init_samples=[Solution(x=initial_params)],
                              exploration_rate=self.options["exploration_rate"], seed=self.options["seed"])
        # optimize
        solution = Opt.min(objective, parameter)
        
        # A LOT OF CUSTOMIZATION CAN BE DONE TO INCLUDE NOISE HANDLING, PARALLELIZATION AND HIGHLY DIM FUNCS
        # num_sre, low_dimension, withdraw_alpha should be set for sequential random embedding
        # num_sre means the number of sequential random embedding
        # low dimension means low dimensional solution space
        #reduce_dim = int(dim_size/10)
        #         parameter = Parameter(budget=budget, high_dimensionality_handling=True, reducedim=True, num_sre=5, 
        #         low_dimension=Dimension(reduce_dim, [self.options["boundaries"]] * reduce_dim, [True] * reduce_dim))

        # save results

        optimization_results = {}
        optimization_results['opt_value'] = solution.get_value()
        optimization_results['opt_params'] = solution.get_x()
        optimization_results['history'] = history
        optimization_results['nfev'] = budget

        return OptimizeResult(optimization_results)