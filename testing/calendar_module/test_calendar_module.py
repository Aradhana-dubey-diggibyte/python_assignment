import pytest

from srs.calendar_module.util import find_day

def test_sample_input():
    assert find_day(8, 5, 2015) == "WEDNESDAY"

def test_leap_year():
    assert find_day(2, 29, 2020) == "SATURDAY"

def test_new_year():
    assert find_day(1, 1, 2000) == "SATURDAY"

def test_random_date():
    assert find_day(12, 25, 2023) == "MONDAY"
