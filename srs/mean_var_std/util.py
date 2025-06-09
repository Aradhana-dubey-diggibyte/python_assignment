import numpy as np

def calculate_mean_var_std(arr):
    arr_np = np.array(arr)
    mean_result = np.mean(arr_np, axis=1)
    var_result = np.var(arr_np, axis=0)
    std_result = np.std(arr_np, axis=None)
    return mean_result, var_result, std_result
