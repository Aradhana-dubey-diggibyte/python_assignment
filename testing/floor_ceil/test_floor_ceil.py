import numpy as np
from srs.floor_ceil.util import apply_floor_ceil_rint

def test_apply_floor_ceil_rint():
    arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
    expected_floor = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
    expected_ceil = np.array([2., 3., 4., 5., 6., 7., 8., 9., 10.])
    expected_rint = np.array([1., 2., 3., 4., 6., 7., 8., 9., 10.])

    floor_vals, ceil_vals, rint_vals = apply_floor_ceil_rint(arr)

    assert np.array_equal(floor_vals, expected_floor)
    assert np.array_equal(ceil_vals, expected_ceil)
    assert np.array_equal(rint_vals, expected_rint)
