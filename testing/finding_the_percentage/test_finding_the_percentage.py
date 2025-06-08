import pytest
from srs.finding_the_percentage.util import find_average

def test_case_1():
    data = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60]
    }
    assert find_average(data, "Malika") == 56.00

def test_case_2():
    data = {
        "Harsh": [25, 26.5, 28],
        "Anurag": [26, 28, 30]
    }
    assert find_average(data, "Harsh") == 26.50

def test_missing_student():
    data = {
        "Harsh": [25, 26.5, 28]
    }
    assert find_average(data, "Anurag") == 0.00
