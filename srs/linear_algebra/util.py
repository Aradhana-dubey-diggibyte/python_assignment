
import numpy as np

def determinant(matrix):
    det_val = np.linalg.det(matrix)
    return round(det_val, 2)
