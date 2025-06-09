
from srs.linear_algebra.util import determinant

def test_determinant():
    matrix = [
        [1.1, 1.1],
        [1.1, 1.1]
    ]
    assert determinant(matrix) == 0.0

    matrix2 = [
        [1, 2],
        [2, 1]
    ]
    assert determinant(matrix2) == -3.0
