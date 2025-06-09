
from srs.no_idea.util import calculate_happiness

def test_calculate_happiness():
    arr = [1, 5, 3]
    A = [3, 1]
    B = [5, 7]
    assert calculate_happiness(arr, A, B) == 1

    arr2 = [1, 2, 3, 4]
    A2 = [1, 2]
    B2 = [3]
    assert calculate_happiness(arr2, A2, B2) == 1  # +1 +1 -1 = 1
