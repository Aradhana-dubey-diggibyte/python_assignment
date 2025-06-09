
import numpy as np

def max_of_min(X, Y, arr):
    """
    Given dimensions X, Y and 2D array arr,
    returns the maximum of the minimums along axis 1.
    """
    arr_np = np.array(arr)
    min_in_rows = np.min(arr_np, axis=1)
    return np.max(min_in_rows)
