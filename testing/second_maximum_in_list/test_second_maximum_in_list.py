import pytest
from srs.second_maximum_in_list.util import find_runner_up_score

def test_runner_up_normal_case():
    assert find_runner_up_score([2, 3, 6, 6, 5]) == 5

def test_runner_up_with_negatives():
    assert find_runner_up_score([-1, -2, -3, -1]) == -2

def test_runner_up_single_value():
    assert find_runner_up_score([5, 5, 5]) is None

def test_runner_up_large_input():
    assert find_runner_up_score([1, 100, 100, 50, 75]) == 75
