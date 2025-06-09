from srs.mean_var_std.util import calculate_mean_var_std
import numpy as np

def test_calculate_mean_var_std():
    arr = [
        [1, 2],
        [3, 4]
    ]
    mean_expected = np.array([1.5, 3.5])
    var_expected = np.array([1., 1.])
    std_expected = 1.11803398875

    mean_result, var_result, std_result = calculate_mean_var_std(arr)

    assert np.allclose(mean_result, mean_expected)
    assert np.allclose(var_result, var_expected)
    assert abs(std_result - std_expected) < 1e-9
