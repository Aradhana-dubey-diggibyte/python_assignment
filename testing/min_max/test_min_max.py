
from srs.min_max.util import max_of_min

def test_max_of_min():
    X = 4
    Y = 2
    arr = [
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ]
    assert max_of_min(X, Y, arr) == 3
