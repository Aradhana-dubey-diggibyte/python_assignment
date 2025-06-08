import pytest
# testing/merge_the_tools/test_merge_the_tools.py

from srs.merge_the_tools.util import merge_the_tools

def test_merge_case1():
    assert merge_the_tools("AABCAAADA", 3) == ['AB', 'CA', 'AD']

def test_merge_case2():
    assert merge_the_tools("AAAA", 2) == ['A', 'A']

def test_merge_case3():
    assert merge_the_tools("ABCDEABCDE", 5) == ['ABCDE', 'ABCDE']

def test_merge_case4():
    assert merge_the_tools("ABABABAB", 2) == ['AB', 'AB', 'AB', 'AB']
