import numpy as np

def apply_floor_ceil_rint(arr):
    arr = np.array(arr, dtype=float)
    return np.floor(arr), np.ceil(arr), np.rint(arr)
